from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from albums.forms import AlbumSearchForm, AlbumForm
from utils.Spotify import Spotify

albums = Blueprint('albums', __name__, url_prefix='/albums', template_folder='templates')

@albums.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = AlbumForm()
    if form.validate_on_submit():
        try:
            result = DB.insert("""INSERT INTO IS601_Albums (album_id, album_name, album_popularity, album_uri, album_img, total_tracks, release_date, label_name)""", 
                        form.album_id.data, form.album_name.data, form.album_popularity.data, form.album_uri.data, form.album_img.data, form.total_tracks.data, form.release_date.data, form.label_name.data)
            if result.status:
                flash(f"Created album record for {form.album_name.data}", "success")
        except Exception as e:
            flash(f"Error creating album record: {e}", "danger")
    return render_template("albums_form.html", form=form, type="Create")

@albums.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = AlbumForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("albums.list"))
    if form.validate_on_submit():
        try:
            result = DB.insert("""UPDATE IS601_Albums SET album_id = %s, album_name = %s, album_popularity = %s, album_uri = %s, album_img = %s, total_tracks = %s, release_date = %s, label_name = %s WHERE id = %s""",
                        form.album_id.data, form.album_name.data, form.album_popularity.data, form.album_uri.data, form.album_img.data, form.total_tracks.data, form.release_date.data, form.label_name.data, id)
            if result.status:
                flash(f"Updated album record for {form.album_name.data}", "success")
        except Exception as e:
            flash(f"Error updating album record: {e}", "danger")
        try:
            result = DB.selectOne(
                "SELECT album_id, album_name, album_type, album_release_date, album_total_tracks, album_img FROM IS601_Albums WHERE id = %s",
                id
            )
            if result.status and result.row:
                return render_template("albums_view.html", albums=result.row)
            else:
                flash("Album record not found", "danger")
        except Exception as e:
            print(f"Albums error {e}")
            flash("Error fetching album record", "danger")
        return redirect(url_for("albums.list"))

@albums.route("/delete", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args ={**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Albums WHERE id = %s", id)
            if result.status:
                flash(f"Deleted album record", "success")
        except Exception as e:
            flash(f"Error deleting album record: {e}", "danger")
        del args["id"]
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("albums.list", **args))

@albums.route("/list")
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, album_id, album_name, album_type, album_release_date, album_total_tracks, album_img FROM IS601_Albums LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
        else:
            flash("No album records found", "warning")
    except Exception as e:
        print(f"Albums error {e}")
        flash("Error fetching album records", "danger")
    return render_template("albums_list.html", rows=rows)

@albums.route("/search", methods=["GET", "POST"])
def search():
    form = AlbumSearchForm()
    if form.validate_on_submit():
        try:
            result = DB.selectAll("SELECT id, album_id, album_name, album_type, album_release_date, album_total_tracks, album_img FROM IS601_Albums WHERE album_name LIKE %s LIMIT 100", f"%{form.album_name.data}%")
            if result.status and result.rows:
                return render_template("albums_list.html", rows=result.rows)
            else:
                flash("No album records found", "warning")
        except Exception as e:
            print(f"Albums error {e}")
            flash("Error fetching album records", "danger")
    return render_template("albums_search.html", form=form)

@albums.route("/view")
def view():
    id = request.args.get("id")
    if id:
        try:
            result = DB.selectOne("SELECT id, album_id, album_name, album_type, album_release_date, album_total_tracks, album_img FROM IS601_Albums WHERE id = %s", id )
            if result.status and result.row:
                return render_template("albums_view.html", albums=result.row)
            else:
                flash("Album record not found", "danger")
        except Exception as e:
            print(f"Albums error {e}")
            flash("Error fetching album record", "danger")
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("albums.list"))
