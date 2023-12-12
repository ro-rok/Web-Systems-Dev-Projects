from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from albums.forms import AlbumSearchForm, AlbumForm, AlbumFetchForm, AlbumSearchSQLForm
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

albums = Blueprint('albums', __name__, url_prefix='/albums', template_folder='templates')

@albums.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    #rk868 - 12/11/23 - This is the add function for albums.
    form = AlbumForm()
    result = None 
    if form.validate_on_submit():
        try:
            uri = f"spotify:album:{form.album_id.data}"
            result = DB.insertOne("""INSERT INTO IS601_Albums (album_id, album_name, album_popularity, album_uri, 
                                album_img, total_tracks, release_date, label_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                album_id = %s, album_name = %s, album_popularity = %s, album_uri = %s, album_img = %s,
                                total_tracks = %s, release_date = %s, label_name = %s""", 
                                form.album_id.data, form.album_name.data, form.album_popularity.data, uri, form.album_img.data, 
                                form.total_tracks.data, form.release_date.data, form.label_name.data)
            if result.status:
                flash(f"Created album record for {form.album_name.data}", "success")
        except Exception as e:
            flash(f"Error creating album record: {e}", "danger")
    return render_template("album_manage.html", form=form, result=result, type="Create")


@albums.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    #rk868 - 12/11/23 - This is the edit function for albums.
    form = AlbumForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("albums.list"))
    if form.validate_on_submit():
        data = form.data
        try:
            uri = f"spotify:album:{form.album_id.data}"
            result = DB.update("""UPDATE IS601_Albums SET album_id = %s, album_name = %s, album_popularity = %s, album_uri = %s, 
                                    album_img = %s, total_tracks = %s, release_date = %s, label_name = %s WHERE id = %s""",
                        form.album_id.data, form.album_name.data, form.album_popularity.data, uri, form.album_img.data, 
                        form.total_tracks.data, form.release_date.data, form.label_name.data, id)
            if result.status:
                flash(f"Updated album record for {form.album_name.data}", "success")
        except Exception as e:
            flash(f"Error updating album record: {e}", "danger")
    result = DB.selectOne(
            "SELECT album_id, album_name, album_popularity, album_uri, album_img, total_tracks, release_date, label_name FROM IS601_Albums WHERE id = %s",
            id
        )
    if result.status and result.row:
        data = DictToObject(result.row)
        form.process(obj=data)

        print(f"Loaded form: {form.data}")
    return render_template("album_manage.html", form=form, type="Edit")

    
@albums.route("/delete", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def delete():
    #rk868 - 12/11/23 - This is the delete function for albums.
    id = request.args.get("id")
    args = {**request.args}
    result = None 
    if id:
        try:
            DB.delete("DELETE FROM IS601_ArtistAlbums WHERE album_id = %s", id)
            flash("Deleted album artist", "success")
        except Exception as e:
            flash(f"Error deleting album genres: {e}", "danger")
        try:
            DB.delete("DELETE FROM IS601_TrackFeatures WHERE track_id IN (SELECT track_id FROM IS601_Tracks WHERE album_id = %s)", id)
        except Exception as e:
            flash(f"Error deleting album track features: {e}", "danger")
        try:
            DB.delete("DELETE FROM IS601_Tracks WHERE album_id = %s", id)
            flash("Deleted album tracks", "success")
        except Exception as e:
            flash(f"Error deleting album tracks: {e}", "danger")
        try:
            result = DB.delete("DELETE FROM IS601_Albums WHERE id = %s", id)
            if result.status:
                flash(f"Deleted album record", "success")
        except Exception as e:
            flash(f"Error deleting album record: {e}", "danger")
        if result and result.status:
            del args["id"]
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("albums.list", **args))


@albums.route("/list", methods=["GET"])
def list():
    #rk868 - 12/11/23 - This is the list function for albums.
    form = AlbumSearchForm(request.args)
    allowed_columns = ["album_name", "release_date", "total_tracks", "album_popularity", "label_name"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT id, album_id, album_name, release_date, total_tracks, album_popularity, label_name
    FROM IS601_Albums
    WHERE 1=1 
    """
    args = {}
    where = ""
    if form.album_name.data:
        args["album_name"] = f"%{form.album_name.data}%"
        where += " AND album_name LIKE %(album_name)s"
    if form.album_total_tracks.data:
        args["album_total_tracks"] = form.album_total_tracks.data
        where += " AND total_tracks = %(album_total_tracks)s"
    if form.label_name.data:
        args["label_name"] = f"%{form.label_name.data}%"
        where += " AND label_name LIKE %(label_name)s"
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
    
    result = DB.selectAll(query + where, args)
    rows = []
    if result.status and result.rows:
        rows = result.rows
    total_records = get_total(""" IS601_Albums""")
    return render_template("albums_list.html", rows=rows, form=form, total_records=total_records)


@albums.route("/search", methods=["GET", "POST"])
def search():
    #rk868 - 12/11/23 - This is the search function for albums.
    form = AlbumSearchSQLForm()
    if form.validate_on_submit():
        #flash(f"Fetching albums with name like {form.album_name.data}", "info")
        name = f"%{form.album_name.data}%"
        print(name)
        try:
            where = "WHERE album_name LIKE %s"
            result = DB.selectAll("SELECT id, album_id, album_name, release_date, total_tracks, album_img FROM IS601_Albums "+ where, name)
            
            if result.status and result.rows:
                return render_template("albums_list.html", rows=result.rows)
            else:
                flash("No album records found", "warning")
        except Exception as e:
            print(f"Albums error {e}")
            flash("Error fetching album records", "danger")
    return render_template("albums_fetch.html", form=form)

@albums.route("/view")
def view():
    #rk868 - 12/11/23 - This is the view function for albums.
    id = request.args.get("id")
    if id:
        result = DB.selectOne("SELECT id, album_id, album_name, release_date, total_tracks, label_name, album_uri, album_img FROM IS601_Albums WHERE id = %s", id)
        if result.status and result.row:
            print(result.row)
            for key, value in result.row.items():
                print(key, value)
            return render_template("albums_view.html", data=result.row)
        else:
            flash("Album record not found", "danger")
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("albums.list"))

@albums.route("/fetch", methods=["GET", "POST"])
def fetch():
    #rk868 - 12/11/23 - This is the fetch function for albums.
    form = AlbumFetchForm()
    if form.validate_on_submit():
        flash(f"Fetching album {form.album_id.data}", "info")
        try:
            print("fetching album", form.album_id.data)
            album = Spotify.get_album(form.album_id.data)
            print(album)
            if album:
                print("loading album")
                SQLLoader.loadAlbum(album)
                id = DB.selectOne("SELECT id FROM IS601_Albums WHERE album_id = %s", form.album_id.data)
                return redirect(url_for("albums.view", id=id.row.get("id")))
            else:
                flash("Album not found", "warning")
        except Exception as e:
            flash(f"Error fetching album: {e}", "danger")
    return render_template("albums_fetch.html", form=form)
