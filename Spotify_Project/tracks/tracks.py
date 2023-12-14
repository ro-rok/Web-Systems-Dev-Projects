from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sql.db import DB 
from roles.permissions import admin_permission
from tracks.forms import AssocForm, TrackSearchForm, TrackForm, TrackFetchForm, TrackSQLSearchForm, AdminTrackSearchForm
from utils.Spotify import Spotify
from utils.SQLLoader import SQLLoader, DictToObject
from datetime import date


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
    del args["id"]
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
    return redirect(url_for("tracks.list", **args))


@tracks.route("/list", methods=["GET"])
def list():
    #rk868 - 12/11/23 - This is the list function for tracks.
    form = TrackSearchForm(request.args)
    allowed_columns = ["track_name","album_name", "track_popularity", "duration_ms", "release_date", "is_explicit" , "track_number"]
    form.sort.choices = [(k, k.replace("_"," ").title()) for k in allowed_columns]
    query = """
    SELECT t.id, t.track_id, a.album_name, t.track_name, t.track_popularity, t.track_number, t.duration_ms, t.is_explicit, t.release_date,
    IFNULL((SELECT COUNT(1) FROM IS601_TrackPlaylist WHERE user_id = %(user_id)s AND track_id = t.id), 0) AS 'is_assoc'  FROM IS601_Tracks t
    LEFT JOIN IS601_Albums a ON t.album_id = a.album_id  WHERE 1=1
    """
    user_id = current_user.id if current_user.is_authenticated else 0
    args = {"user_id": user_id}
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
    total_records = get_total("IS601_Tracks t LEFT JOIN IS601_Albums a ON t.album_id = a.album_id WHERE 1=1")
    return render_template("tracks_list.html", rows=rows, form=form, total_records=total_records)


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
    in_playlist = 0
    if id:
        track = DB.selectOne("""SELECT t.id, t.track_id, a.album_name, a.id as album_id, t.track_name, t.duration_ms, t.is_explicit, t.release_date,
                                t.track_popularity, t.preview_url, t.track_number, t.track_uri, t.track_img
                                FROM IS601_Tracks t LEFT JOIN IS601_Albums a ON t.album_id = a.album_id WHERE t.id = %s""", id)
        #print("track", track)
        if track.status and track.row:
            album_id = track.row.get("album_id")
            album_artist= DB.selectAll("""SELECT a.artist_name, aa.artist_id FROM IS601_ArtistAlbums aa LEFT JOIN IS601_Artists a ON aa.artist_id = a.id WHERE aa.album_id = %s""", album_id)
            print("album_artist", album_artist)
            featuring = DB.selectAll("""SELECT a.artist_name, aa.artist_id FROM IS601_TrackFeatures aa LEFT JOIN IS601_Artists a ON aa.artist_id = a.id WHERE aa.track_id = %s""", id)
            print("featuring", featuring)
            if album_artist.status:
                if current_user.is_authenticated:
                    in_playlist = DB.selectOne("""SELECT COUNT(1) as total FROM IS601_TrackPlaylist WHERE track_id = %s AND user_id = %s""", track.row.get("id"), current_user.id)
                    print("in_playlist", in_playlist)
                return render_template("tracks_view.html", track=track.row, album_artists=album_artist.rows , in_playlist=in_playlist.row.get("total") if in_playlist and in_playlist.status else 0, featuring=featuring.rows if featuring and featuring.status else [])
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

@tracks.route("/record", methods=["GET"])
@login_required
def record():
    #rk868 - 12/12/23 - This is the function to record the tracks in the playlist.
    id = request.args.get("id")
    args = {**request.args}
    del args["id"]
    if not id:
        flash("Missing id parameter", "danger")
    else:
        params = {"user_id": current_user.id, "track_id": id}
        try:
            try:
                result = DB.insertOne("INSERT INTO IS601_TrackPlaylist (track_id, user_id) VALUES (%(track_id)s, %(user_id)s)", params)
                if result.status:
                    flash("Added track to your Playlist", "success")
            except Exception as e:
                print(f"Should just be a duplicate exception and can be ignored {e}")
                result = DB.delete("DELETE FROM IS601_TrackPlaylist WHERE track_id = %(track_id)s AND user_id = %(user_id)s", params)
                if result.status:
                    flash("Removed track from your Playlist", "success")
        except Exception as e:
            print(f"Error doing something with track/untrack {e}")
            flash("An unhandled error occurred please try again" ,"danger")

    url = request.referrer
    if url:
        from urllib.parse import urlparse
        url_stuff = urlparse(url)
        playlist_url = url_for("tracks.playlist")
        print(f"Parsed url {url_stuff} {playlist_url}")
        if url_stuff.path == url_for("tracks.playlist"):
            return redirect(url_for("tracks.playlist", **args))
        elif url_stuff.path == url_for("tracks.view"):
            args["id"] = id
            return redirect(url_for("tracks.view", **args))
    return redirect(url_for("tracks.list", **args))


@tracks.route("/playlist", methods=["GET"])
def playlist():
    #rk868 - 12/12/23 - This is the function to display the tracks in the playlist.
    id = request.args.get("id", current_user.id)

    form = TrackSearchForm(request.args)
    allowed_columns = ["track_name","album_name", "track_popularity", "duration_ms", "release_date", "is_explicit" , "track_number"]
    form.sort.choices = [(k, k.replace("_"," ").title()) for k in allowed_columns]
    query = """
    SELECT t.id, t.track_id, a.album_name, t.track_name, t.track_popularity, t.track_number, t.duration_ms, t.is_explicit, t.release_date,
    1 AS 'is_assoc'
    FROM IS601_Tracks t JOIN IS601_TrackPlaylist tp ON t.id = tp.track_id
    LEFT JOIN IS601_Albums a ON t.album_id = a.album_id
    WHERE tp.user_id = %(user_id)s
    """
    args = {"user_id": id}
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
    total_records = get_total(""" IS601_Tracks t JOIN IS601_TrackPlaylist tp ON t.id = tp.track_id
                                    WHERE tp.user_id = %(user_id)s""", {"user_id": id})
    return render_template("tracks_list.html", rows=rows, form=form, title="Playlist", total_records=total_records)

@tracks.route("/clear", methods=["GET"])
def clear():
    #rk868 - 12/12/23 - This is the function to clear the tracks in the playlist.
    id = request.args.get("id")
    args = {**request.args}
    if "id" in args:
        del args["id"]
    if not id:
        flash("Missing id", "danger")
    else:
        if id == current_user.id or current_user.has_role("Admin"):
            try:
                result = DB.delete("DELETE FROM IS601_TrackPlaylist WHERE user_id = %(user_id)s", {"user_id":id})
                if result.status:
                    flash("Cleared playlist", "success")
            except Exception as e:
                print(f"Error clearing playlist {e}")
                flash("Error clearing playlist","danger")
    return redirect(url_for("tracks.playlist", **args))

@tracks.route("/associate", methods=["GET"])
@admin_permission.require(http_exception=403)
def associations():
    #rk868 - 12/13/23 - This is the function to display the associations in the playlist.
    form = AdminTrackSearchForm(request.args)
    allowed_columns = ["track_name","album_name", "track_popularity", "duration_ms", "release_date", "is_explicit" , "track_number"]
    form.sort.choices = [(k, k.replace("_"," ").title()) for k in allowed_columns]
    query = """
    SELECT u.id as user_id, username, t.id, t.track_id, a.album_name, t.track_name, t.track_popularity, t.track_number, t.duration_ms, t.is_explicit, t.release_date
    FROM IS601_Tracks t JOIN IS601_TrackPlaylist tp ON t.id = tp.track_id 
    LEFT JOIN IS601_Users u ON u.id = tp.user_id
    LEFT JOIN IS601_Albums a ON t.album_id = a.album_id
    WHERE 1=1
    """
    args = {}
    where = ""
    if form.username.data:
        args["username"] = f"%{form.username.data}%"
        where += " AND username LIKE %(username)s"
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
    total_records = get_total("IS601_Tracks t JOIN IS601_TrackPlaylist tp ON t.id = tp.track_id WHERE 1=1")
    return render_template("tracks_list.html", rows=rows, form=form, title="Associations", total_records=total_records)

@tracks.route("/unwatched", methods=["GET"])
@login_required
def unwatched():
    #rk868 - 12/13/23 - This is the function to display the not selected tracks in the playlist.
    form = TrackSearchForm(request.args)
    allowed_columns = ["track_name","album_name", "track_popularity", "duration_ms", "release_date", "is_explicit" , "track_number"]
    form.sort.choices = [(k, k.replace("_"," ").title()) for k in allowed_columns]
    query = """
    SELECT t.id, t.track_id, a.album_name, t.track_name, t.track_popularity, t.track_number, t.duration_ms, t.is_explicit, t.release_date,
    IFNULL((SELECT COUNT(1) FROM IS601_TrackPlaylist WHERE user_id = %(user_id)s AND track_id = t.id), 0) AS 'is_assoc'
    FROM IS601_Tracks t
    LEFT JOIN IS601_Albums a ON t.album_id = a.album_id
    WHERE t.id NOT IN (SELECT track_id FROM IS601_TrackPlaylist)
    """
    args = {"user_id": current_user.id}
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
    total_records = get_total("IS601_Tracks t LEFT JOIN IS601_Albums a ON t.album_id = a.album_id WHERE t.id NOT IN (SELECT DISTINCT track_id FROM IS601_TrackPlaylist)") 
    return render_template("tracks_list.html", rows=rows, form=form, title="Unwatched Items", total_records=total_records)

@tracks.route("/manage", methods=["GET"])
def manage():
    #rk868 - 12/13/23 - This is the manage function for tracks.
    form = AssocForm(request.args)
    users = []
    tracks = []
    username = form.username.data
    track_name = form.track_name.data
    if username and track_name:
        result = DB.selectAll("SELECT id, username FROM IS601_Users WHERE username LIKE %(username)s ORDER BY RAND() LIMIT 25", {"username": f"%{username}%"})
        if result.status and result.rows:
            users = result.rows
        result = DB.selectAll("SELECT id, track_name FROM IS601_Tracks WHERE track_name LIKE %(track)s ORDER BY RAND() LIMIT 25", {"track": f"%{track_name}%"})
        if result.status and result.rows:
            tracks = result.rows
    else:
        result = DB.selectAll("SELECT id, username FROM IS601_Users ORDER BY RAND() LIMIT 25")
        if result.status and result.rows:
            users = result.rows
        result = DB.selectAll("SELECT id, track_name, preview_url, track_id FROM IS601_Tracks ORDER BY RAND() LIMIT 25")
        if result.status and result.rows:
            tracks = result.rows
    print(f"Users: {users}")
    print(f"Tracks: {tracks}")
    return render_template("track_association.html", users=users, tracks=tracks, form=form)


@tracks.route("/manage_assoc", methods=["POST"])
def manage_assoc():
    #rk868 - 12/13/23 - This is the manage_assoc function for tracks.
    users = request.form.getlist("users[]")
    tracks = request.form.getlist("tracks[]")
    print(users, tracks)
    args = {**request.args}
    if users and tracks: 
        mappings = []
        for user in users:
            for track in tracks:
                mappings.append({"user_id":user, "track_id":track})
        if len(mappings) > 0:
            ad = 0
            su = 0
            for mapping in mappings:
                print(f"mapping {mapping}")
                try:
                    result = DB.insertOne("INSERT INTO IS601_TrackPlaylist (user_id, track_id) VALUES(%(user_id)s, %(track_id)s)", mapping)
                    if result.status:
                        ad += 1
                        
                except Exception as e:
                    print(f"Insert error {e}")
                    result = DB.delete("DELETE FROM IS601_TrackPlaylist WHERE user_id = %(user_id)s and track_id = %(track_id)s",mapping)
                    if result.status:
                        su += 1
            msg = "Successfully"
            msg += f" added: {ad} " if ad > 0 else ""
            msg += f" removed: {su} " if su > 0 else ""
            msg += " associations"
            flash(msg, "success")            
        else:
            flash("No user/track mappings", "danger")

    if "users" in args:
        del args["users"]
    if "tracks" in args:
        del args["tracks"]
    return redirect(url_for("tracks.manage", **args))
