from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from artists.forms import ArtistSearchForm, ArtistForm, ArtistFetchForm
from utils.Spotify import Spotify
from utils.SQLLoader import SQLLoader

artists = Blueprint('artists', __name__, url_prefix='/artists', template_folder='templates')

@artists.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = ArtistForm()
    result = None  # Add this line to define the 'result' variable
    if form.validate_on_submit():
        try:
            result = DB.insert("""INSERT INTO IS601_Artists (artist_id, artist_name, artist_popularity,  followers_total, artist_uri, artist_img)""", 
                        form.artist_id.data, form.artist_name.data, form.artist_popularity.data,  form.followers_total.data, form.artist_uri.data, form.artist_img.data)
            if result.status:
                flash(f"Created artist record for {form.artist_name.data}", "success")
        except Exception as e:
            flash(f"Error creating artist record: {e}", "danger")
    return render_template("artists_form.html", form=form, result=result)  # Pass 'result' to the template context

@artists.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = ArtistForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("artists.list"))
    if form.validate_on_submit():
        try:
            result = DB.insert("""UPDATE IS601_Artists SET artist_id = %s, artist_name = %s, artist_popularity = %s,  followers_total = %s, artist_uri = %s, artist_img = %s WHERE id = %s""",
                        form.artist_id.data, form.artist_name.data, form.artist_popularity.data,  form.followers_total.data, form.artist_uri.data, form.artist_img.data, id)
            if result.status:
                flash(f"Updated artist record for {form.artist_name.data}", "success")
        except Exception as e:
            flash(f"Error updating artist record: {e}", "danger")
        try:
            result = DB.selectOne(
                "SELECT artist_id, artist_name, artist_popularity,  followers_total, artist_uri, artist_img FROM IS601_Artists WHERE id = %s",
                id
            )
            if result.status and result.row:
                return render_template("artists_view.html", artists=result.row)
            else:
                flash("Artist record not found", "danger")
        except Exception as e:
            print(f"Artists error {e}")
            flash("Error fetching artist record", "danger")
        return redirect(url_for("artists.list"))

@artists.route("/delete", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args ={**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Artists WHERE id = %s", id)
            if result.status:
                flash(f"Deleted artist record", "success")
        except Exception as e:
            flash(f"Error deleting artist record: {e}", "danger")
        del args["id"]
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("artists.list", **args))

@artists.route("/list")
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, artist_id, artist_name, artist_popularity,  followers_total, artist_uri, artist_img FROM IS601_Artists LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
        else:
            flash("No artist records found", "warning")
    except Exception as e:
        print(f"Artists error {e}")
        flash("Error fetching artist records", "danger")
    return render_template("artists_list.html", rows=rows)

@artists.route("/search", methods=["GET", "POST"])
def search():
    form = ArtistSearchForm()
    if form.validate_on_submit():
        try:
            result = DB.selectAll("SELECT id, artist_id, artist_name, artist_popularity,  followers_total, artist_uri, artist_img FROM IS601_Artists WHERE artist_name LIKE %s LIMIT 100", f"%{form.artist_name.data}%")
            if result.status and result.rows:
                return render_template("artists_list.html", rows=result.rows)
            else:
                flash("No artist records found", "warning")
        except Exception as e:
            print(f"Artists error {e}")
            flash("Error fetching artist records", "danger")
    return render_template("artists_search.html", form=form)

@artists.route("/view")
def view():
    id = request.args.get("artist_id")
    if id:
        try:
            result = DB.selectOne("SELECT id, artist_id, artist_name, artist_popularity, followers_total, artist_uri, artist_img FROM IS601_Artists WHERE artist_id = %s", id )
            if result.status and result.row:
                return render_template("artists_view.html", artists=result.row)
            else:
                flash("Artist record not found", "danger")
        except Exception as e:
            print(f"Artists error {e}")
            flash("Error fetching artist record", "danger")
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("artists.list"))

@artists.route("/fetch", methods=["GET", "POST"])
def fetch():
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

                return url_for("artists.view", artist_id=form.artist_id.data)
            else:
                flash("Artist not found", "warning")
        except Exception as e:
            flash(f"Error fetching artist: {e}", "danger")
    return render_template("artists_search.html", form=form)
