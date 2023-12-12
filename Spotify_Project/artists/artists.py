from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from artists.forms import ArtistSearchForm, ArtistForm, ArtistFetchForm, ArtistSQLSearchForm
from utils.Spotify import Spotify
from utils.SQLLoader import SQLLoader, DictToObject

def get_total(partial_query, args={}):
    total = 0
    try:
        result = DB.selectOne("SELECT count(1) as total FROM "+partial_query, args)
        if result.status and result.row:
            total = int(result.row["total"])
    except Exception as e:
        print(f"Error getting total {e}")
        total = 0
    return total

artists = Blueprint('artists', __name__, url_prefix='/artists', template_folder='templates')



@artists.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    #rk868 - 12/10/23 - This is the add function for artists.
    form = ArtistForm()
    result = None 
    if form.validate_on_submit():
        try:
            uri = f"spotify:artist:{form.artist_id.data}"
            print(form.artist_id.data, form.artist_name.data, form.artist_popularity.data,  form.followers_total.data, uri, form.artist_img.data)
            result = DB.insertOne("""INSERT INTO IS601_Artists (artist_id, artist_name, artist_popularity,  followers_total, artist_uri, artist_img)
                                    VALUES (%s, %s, %s, %s, %s, %s)
                                    ON DUPLICATE KEY UPDATE
                                    artist_id = %s, artist_name = %s, artist_popularity = %s,  followers_total = %s, artist_uri = %s, artist_img = %s""", 
                        form.artist_id.data, form.artist_name.data, form.artist_popularity.data,  form.followers_total.data, uri, form.artist_img.data)
            if result.status:
                flash(f"Created artist record for {form.artist_name.data}", "success")
        except Exception as e:
            flash(f"Error creating artist record: {e}", "danger")
    return render_template("artist_manage.html", form=form, result=result, type="Create")




@artists.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    #rk868 - 12/10/23 - This is the edit function for artists.
    form = ArtistForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("artists.list"))
    if form.validate_on_submit():
        data = form.data
        try:
            uri = f"spotify:artist:{form.artist_id.data}"
            result = DB.update("""UPDATE IS601_Artists SET artist_id = %s, artist_name = %s, artist_popularity = %s,  followers_total = %s, artist_uri = %s, artist_img = %s WHERE id = %s""",
                        form.artist_id.data, form.artist_name.data, form.artist_popularity.data,  form.followers_total.data, uri, form.artist_img.data, id)
            if result.status:
                flash(f"Updated artist record for {form.artist_name.data}", "success")
        except Exception as e:
            flash(f"Error updating artist record: {e}", "danger")
    result = DB.selectOne(
            "SELECT artist_id, artist_name, artist_popularity,  followers_total, artist_uri, artist_img FROM IS601_Artists WHERE id = %s",
            id
        )
    if result.status and result.row:
        data = DictToObject(result.row)
        form.process(obj=data)

        print(f"Loaded form: {form.data}")
    return render_template("artist_manage.html", form=form, type="Edit")

@artists.route("/delete", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def delete():
    #rk868 - 12/10/23 - This is the delete function for artists.
    id = request.args.get("id")
    args = {**request.args}
    result = None
    if id:
        try:
            DB.delete("DELETE FROM IS601_ArtistGenres WHERE artist_id = %s", id)
            flash("Deleted artist genres", "success")
        except Exception as e:
            flash(f"Error deleting artist genres: {e}", "danger")

        try:
            DB.delete("DELETE FROM IS601_ArtistAlbums WHERE artist_id = %s", id)
            flash("Deleted artist albums", "success")
        except Exception as e:
            flash(f"Error deleting artist albums: {e}", "danger")

        try:
            result = DB.delete("DELETE FROM IS601_Artists WHERE id = %s", id)
            if result.status:
                flash(f"Deleted artist record", "success")
        except Exception as e:
            flash(f"Error deleting artist record: {e}", "danger")

        if result and result.status:
            del args["id"]
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("artists.list", **args))

@artists.route("/list" , methods=["GET"])
def list():
    #rk868 - 12/10/23 - This is the list function for artists.
    form = ArtistSearchForm(request.args)
    allowed_columns = ["artist_name", "artist_popularity", "followers_total"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT id, artist_id, artist_name, artist_popularity, followers_total
    FROM IS601_Artists
    WHERE 1=1 AND followers_total IS NOT NULL
    """
    args = {}
    where = ""
    if form.artist_name.data:
        args["artist_name"] = f"%{form.artist_name.data}%"
        where += " AND artist_name LIKE %(artist_name)s"
    if form.artist_popularity.data:
        args["artist_popularity"] = form.artist_popularity.data
        where += " AND artist_popularity = %(artist_popularity)s"
    if form.followers_total.data:
        args["followers_total"] = form.followers_total.data
        where += " AND followers_total = %(followers_total)s"
    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"
    
    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"
    
    result = DB.selectAll(query+where, args)
    rows = []
    if result.status and result.rows:
        rows = result.rows
    total_records = get_total(""" IS601_Artists""")
    return render_template("artists_list.html", rows=rows, form=form, total_records=total_records)

@artists.route("/search", methods=["GET", "POST"])
def search():
    #rk868 - 12/10/23 - This is the search function for artists.
    form = ArtistFetchForm()
    if form.validate_on_submit():
        try:
            result = DB.selectAll("SELECT id, artist_id, artist_name, artist_popularity, followers_total FROM IS601_Artists WHERE artist_name LIKE %s LIMIT 100", f"%{form.artist_id.data}%")
            if result.status and result.rows:
                return render_template("artists_list.html", rows=result.rows)
            else:
                flash("No artist records found", "warning")
        except Exception as e:
            print(f"Artists error {e}")
            flash("Error fetching artist records", "danger")
    return render_template("artists_fetch.html", form=form)

@artists.route("/view")
def view():
    #rk868 - 12/10/23 - This is the view function for artists.
    id = request.args.get("id")
    if id:
            result = DB.selectOne("SELECT id, artist_id, artist_name, artist_popularity, followers_total, artist_uri, artist_img FROM IS601_Artists WHERE id = %s", id )
            if result.status and result.row:
                print(result.row)  
                for key, value in result.row.items():
                    print(key, value)
                return render_template("artists_view.html", data=result.row)
            else:
                flash("Artist record not found", "danger")
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("artists.list"))

@artists.route("/fetch", methods=["GET", "POST"])
def fetch():
    #rk868 - 12/10/23 - This is the fetch function for artists.
    form = ArtistFetchForm()
    if form.validate_on_submit():
        flash(f"Fetching artist {form.artist_id.data}", "info")
        try:
            print("fetching artist", form.artist_id.data)
            artist = Spotify.get_artist(form.artist_id.data)
            print(artist)
            if artist:
                print("loading artist")
                SQLLoader.loadArtist(artist)
                id = DB.selectOne("SELECT id FROM IS601_Artists WHERE artist_id = %s", form.artist_id.data)
                return redirect(url_for("artists.view", id=id.row.get("id")))
            else:
                flash("Artist not found", "warning")
        except Exception as e:
            flash(f"Error fetching artist: {e}", "danger")
    return render_template("artists_fetch.html", form=form)
