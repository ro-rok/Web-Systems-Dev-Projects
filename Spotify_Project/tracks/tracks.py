from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from tracks.forms import TrackSearchForm, TrackForm
from utils.Spotify import Spotify

tracks = Blueprint('tracks', __name__, url_prefix='/tracks', template_folder='templates')

@tracks.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    """Add a new tracks record to the database from the form"""
    form = TrackForm()
    if form.validate_on_submit():
        try:
            result = DB.insert("""INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                        form.track_id.data, form.album_id.data, form.track_name.data, form.track_popularity.data, form.preview_url.data, form.track_number.data, 
                        form.track_uri.data, form.track_img.data, form.duration_ms.data, form.is_explicit.data, form.release_date.data)
            if result.status:
                flash(f"Created track record for {form.track_name.data}", "success")
        except Exception as e:
            flash(f"Error creating track record: {e}", "danger")
    return render_template("tracks_form.html", form=form, type="Create")

@tracks.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    """Edit an existing tracks record in the database from the form"""
    form = TrackForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("tracks.list"))
    if form.validate_on_submit():
        try:
            result = DB.insert("""UPDATE IS601_Tracks SET track_id = %s, album_id = %s, track_name = %s, track_popularity = %s, preview_url = %s, track_number = %s, track_uri = %s, track_img = %s, duration_ms = %s, is_explicit = %s, release_date = %s WHERE id = %s""",
                        form.track_id.data, form.album_id.data, form.track_name.data, form.track_popularity.data, form.preview_url.data, form.track_number.data, 
                        form.track_uri.data, form.track_img.data, form.duration_ms.data, form.is_explicit.data, form.release_date.data, id)
            if result.status:
                flash(f"Updated track record for {form.track_name.data}", "success")
        except Exception as e:
            flash(f"Error updating track record: {e}", "danger")
        try:
            result = DB.selectOne(
                "SELECT track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date FROM IS601_Tracks WHERE id = %s",
                id
            )
            if result.status and result.row:
                return render_template("tracks_view.html", tracks=result.row)
            else:
                flash("tracks record not found", "danger")
        except Exception as e:
            print(f"Tracks error {e}")
            flash("Error fetching tracks record", "danger")
        return redirect(url_for("tracks.list"))

@tracks.route("/delete", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def delete():
    """Delete an existing tracks record from the database"""
    id = request.args.get("id")
    args ={**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Tracks WHERE id = %s", id)
            if result.status:
                flash(f"Deleted tracks record", "success")
        except Exception as e:
            flash(f"Error deleting tracks record: {e}", "danger")
        del args["id"]
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("tracks.list", **args))

@tracks.route("/list")
@admin_permission.require(http_exception=403)
def list():
    """List tracks records from the database"""
    rows = []
    try:
        result = DB.selectAll("SELECT id, track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date FROM IS601_Tracks LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
        else:
            flash("No tracks records found", "warning")
    except Exception as e:
        print(f"Tracks error {e}")
        flash("Error fetching tracks records", "danger")
    return render_template("tracks_list.html", rows=rows)

@tracks.route("/search", methods=["GET", "POST"])
def search():
    """Search tracks records from the database"""
    form = TrackSearchForm()
    if form.validate_on_submit():
        try:
            result = DB.selectAll("SELECT id, track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date FROM IS601_Tracks WHERE track_name LIKE %s LIMIT 100", f"%{form.query.data}%")
            if result.status and result.rows:
                return render_template("tracks_list.html", rows=result.rows)
            else:
                flash("No tracks records found", "warning")
        except Exception as e:
            print(f"Tracks error {e}")
            flash("Error fetching tracks records", "danger")
    return render_template("tracks_search.html", form=form)

@tracks.route("/view")
def view():
    id = request.args.get("id")
    if id:
        try:
            result = DB.selectOne(
                "SELECT track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date FROM IS601_Tracks WHERE id = %s",
                id
            )
            if result.status and result.row:
                return render_template("tracks_view.html", tracks=result.row)
            else:
                flash("tracks record not found", "danger")
        except Exception as e:
            print(f"Tracks error {e}")
            flash("Error fetching tracks record", "danger")
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("tracks.list"))

