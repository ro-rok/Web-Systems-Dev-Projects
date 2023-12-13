from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from tracks.forms import TrackSearchForm, TrackForm, TrackFetchForm, TrackSQLSearchForm
from utils.Spotify import Spotify
from utils.SQLLoader import SQLLoader, DictToObject


tracks = Blueprint('tracks', __name__, url_prefix='/tracks', template_folder='templates')

def get_albums():
    #rk868 - 12/11/23 - This is the get_albums function for tracks.
    results = DB.selectAll(" SELECT album_id, album_name FROM IS601_Albums")
    r = []
    if results.status and results.rows:
        r = results.rows
    return r

def get_artists():
    #rk868 - 12/11/23 - This is the get_artists function for tracks.
    results = DB.selectAll(" SELECT id, artist_name FROM IS601_Artists")
    r = []
    if results.status and results.rows:
        r = results.rows
    return r

@tracks.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    #rk868 - 12/11/23 - This is the add function for tracks.
    form = TrackForm()
    albums = [(r["album_id"], r["album_name"]) for r in get_albums()]
    form.album_id.choices = albums
    artists =[(None, "Select Featuring" )]+ [(r["id"], r["artist_name"]) for r in get_artists()]
    form.artist_id.choices = artists
    result = None

    if form.validate_on_submit():
        try:
            try:
                uri = f"spotify:album:{form.album_id.data}"
                #print(f"Track data: {form.track_id.data}, album: {form.album_id.data}, Name: {form.track_name.data}, {form.track_popularity.data}, {form.preview_url.data}, {form.track_number.data}, {uri}, {form.track_img.data}, {form.duration_ms.data}, {form.is_explicit.data}, {form.release_date.data}")
                albums_id = form.album_id.data
                print("album id", albums_id)
                result = DB.insertOne("""INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        ON DUPLICATE KEY UPDATE
                                        track_id = values(track_id), album_id = values(album_id), track_name = values(track_name), track_popularity = values(track_popularity), preview_url = values(preview_url), 
                                        track_number = values(track_number), track_uri = values(track_uri), track_img = values(track_img), duration_ms = values(duration_ms), is_explicit = values(is_explicit), release_date = values(release_date) """,
                                        form.track_id.data, form.album_id.data, form.track_name.data, form.track_popularity.data, form.preview_url.data, form.track_number.data,
                                        uri, form.track_img.data, form.duration_ms.data, form.is_explicit.data, form.release_date.data)
            except Exception as e:
                flash(f"Error creating track record: {e}", "danger")
            try:
                id = DB.selectOne("""SELECT id FROM IS601_Tracks WHERE track_id = %s""", form.track_id.data)
                if id.status and id.row and form.artist_id.data is not None:
                    result1 = DB.insertOne("""INSERT INTO IS601_TrackFeatures (track_id, artist_id) VALUES (%s, %s)
                                            ON DUPLICATE KEY UPDATE
                                            track_id = %s, artist_id = %s
                                            """, id.row.get("id"), form.artist_id.data, id.row.get("id"), form.artist_id.data)
            except Exception as e:
                flash(f"Error creating track record: {e}", "danger")
            if result and result.status:
                flash(f"Created track record for {form.track_name.data}", "success")
        except Exception as e:
            flash(f"Error creating track record: {e}", "danger")

    return render_template("tracks_manage.html", form=form, type="Create")

@tracks.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    #rk868 - 12/11/23 - This is the edit function for tracks.
    form = TrackForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("tracks.list"))
    albums = [(r["album_id"], r["album_name"]) for r in get_albums()]
    form.album_id.choices = albums
    artists = [(r["id"], r["artist_name"]) for r in get_artists()]
    form.artist_id.choices = artists
    if form.validate_on_submit():
        data = form.data
        try:
            uri = f"spotify:album:{form.album_id.data}"
            result = DB.update("""UPDATE IS601_Tracks SET track_id = %s, album_id = %s, track_name = %s, track_popularity = %s, preview_url = %s, 
                                track_number = %s, track_uri = %s, track_img = %s, duration_ms = %s, is_explicit = %s, release_date = %s WHERE id = %s""",
                        form.track_id.data, form.album_id.data, form.track_name.data, form.track_popularity.data, form.preview_url.data, form.track_number.data,
                        uri, form.track_img.data, form.duration_ms.data, form.is_explicit.data, form.release_date.data, id)
            result1 = DB.update("""UPDATE IS601_TrackFeatures SET track_id = %s, artist_id = %s WHERE track_id = %s""", id, form.artist_id.data, id)
            if result.status and result1.status:
                flash(f"Updated track record for {form.track_name.data}", "success")
        except Exception as e:
            flash(f"Error updating track record: {e}", "danger")
    result = DB.selectOne(
            "SELECT track_id, album_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date FROM IS601_Tracks WHERE id = %s",
            id
        )
    if result.status and result.row:
        data = DictToObject(result.row)
        form.process(obj=data)

        print(f"Loaded form: {form.data}")
    else:
        flash("Track not found", "danger")
        return redirect(url_for("tracks.list"))
    return render_template("tracks_manage.html", form=form, type="Edit")


@tracks.route("/delete", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def delete():
    #rk868 - 12/11/23 - This is the delete function for tracks.
    id = request.args.get("id")
    args = {**request.args}
    filter_criteria = {
        "track_name": args.get("track_name"),
        "track_popularity": args.get("track_popularity"),
        "is_explicit": args.get("is_explicit"),
        "album_name": args.get("album_name"),
        "sort": args.get("sort"),
        "order": args.get("order")
    }
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_TrackFeatures WHERE track_id = %s", id)
            result1 = DB.delete("DELETE FROM IS601_Tracks WHERE id = %s", id)
            if result.status and result1.status:
                flash("Deleted tracks record", "success")
            else:
                flash("Error deleting tracks record", "danger")
        except Exception as e:
            flash(f"Error deleting tracks record: {e}", "danger")
        del args["id"]
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("tracks.list", **args, **filter_criteria))


@tracks.route("/list", methods=["GET"])
def list():
    #rk868 - 12/11/23 - This is the list function for tracks.
    form = TrackSearchForm(request.args)
    allowed_columns = ["track_name","album_name", "track_popularity", "duration_ms", "release_date", "is_explicit" , "track_number"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT t.id, t.track_id, a.album_name, t.track_name, t.track_popularity, t.track_number, t.duration_ms, t.is_explicit, t.release_date FROM IS601_Tracks t
    LEFT JOIN IS601_Albums a ON t.album_id = a.album_id
    WHERE 1=1
    """
    args = {}
    where = ""
    if form.track_name.data:
        args["track_name"] = f"%{form.track_name.data}%"
        where += " AND t.track_name LIKE %(track_name)s"
    if form.track_popularity.data:
        args["track_popularity"] = form.track_popularity.data
        where += " AND t.track_popularity = %(track_popularity)s"
    if form.is_explicit.data:
        args["is_explicit"] = form.is_explicit.data
        where += " AND t.is_explicit = %(is_explicit)s"
    if form.album_name.data:
        args["album_name"] = f"%{form.album_name.data}%"
        where += " AND a.album_name LIKE %(album_name)s"
    
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
    return render_template("tracks_list.html", rows=rows, form=form)


@tracks.route("/search", methods=["GET", "POST"])
def search():
    #rk868 - 12/11/23 - This is the search function for tracks.
    form = TrackSQLSearchForm()
    if form.validate_on_submit():
        try:
            result = DB.selectAll("SELECT id, track_id, track_name, track_popularity, preview_url, track_number, track_uri, track_img, duration_ms, is_explicit, release_date FROM IS601_Tracks WHERE track_name LIKE %s LIMIT 100", f"%{form.track_name.data}%")
            if result.status and result.rows:
                return render_template("tracks_list.html", rows=result.rows, form=form)
            else:
                flash("No tracks found", "danger")
        except Exception as e:
            print(f"Tracks error {e}")
            flash("Error fetching tracks records", "danger")
    return render_template("tracks_fetch.html", form=form)

@tracks.route("/view")
def view():
    #rk868 - 12/11/23 - This is the view function for tracks.
    id = request.args.get("id")
    if id:
        track = DB.selectOne("""SELECT t.id, t.track_id, a.album_name, a.id as album_id, t.track_name, 
                                t.track_popularity, t.preview_url, t.track_number, t.track_uri, t.track_img, 
                                t.duration_ms, t.is_explicit
                                FROM IS601_Tracks t LEFT JOIN IS601_Albums a ON t.album_id = a.album_id WHERE t.id = %s""", id)
        print("track", track)
        if track.status and track.row:
            album_id = track.row.get("album_id")
            album_artist= DB.selectOne("""SELECT a.artist_name FROM IS601_ArtistAlbums aa LEFT JOIN IS601_Artists a ON aa.artist_id = a.id WHERE aa.album_id = %s""", album_id)
            if album_artist.status:
                artist_id = DB.selectOne("""SELECT id FROM IS601_Artists WHERE artist_name = %s""", album_artist.row.get("artist_name"))
                return render_template("tracks_view.html", track=track.row, album_artist=album_artist.row , artist_id=artist_id.row.get("id"))
        else:
            flash("No track found", "danger")
    else:
        flash("Missing ID", "danger")
    return redirect(url_for("tracks.list"))

@tracks.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    #rk868 - 12/11/23 - This is the fetch function for tracks.
    form = TrackFetchForm()
    if form.validate_on_submit():
        flash(f"Fetching track {form.track_id.data}", "info")
        try:
            print("fetching track", form.track_id.data)
            track = Spotify.get_track(form.track_id.data)
            print(track)
            if track:
                print("loading track")
                SQLLoader.loadTrack(track)
                id = DB.selectOne("SELECT id FROM IS601_Tracks WHERE track_id = %s", form.track_id.data)
                return redirect(url_for("tracks.view", id=id.row.get("id")))
            else:
                flash("Track not found", "warning")
        except Exception as e:
            flash(f"Error fetching track: {e}", "danger")
    return render_template("tracks_fetch.html", form=form)