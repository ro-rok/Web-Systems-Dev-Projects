from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from root.forms import SearchForm
from utils.Spotify import Spotify
from utils.SQLLoader import SQLLoader

root = Blueprint('root', __name__, url_prefix='', template_folder='templates')

def checker(uri):
    #rk868 - 12/10/23 - This is the checker function if the artist, album, or track is already in the database.
    spotify_id = uri.split(":")[-1]
    type = uri.split(":")[-2].capitalize()
    query = f"SELECT id FROM IS601_{type}s WHERE {type}_id = %s"
    result = DB.selectOne(query, spotify_id)
    print(result)
    if result.status and result.row:
        print(result.row.get("id"))
        return result.row.get("id")
    else:
        return None

def api_call(uri):
    #rk868 - 12/10/23 - This is the api_call function for the artist, album, or track.
    spotify_id = uri.split(":")[-1]
    if "artist" in uri:
        artist = Spotify.get_artist(spotify_id)
        if artist:
            print("loading artist")
            SQLLoader.loadArtist(artist)
            id = DB.selectOne("SELECT id FROM IS601_Artists WHERE artist_id = %s", spotify_id)
            return redirect(url_for("artists.view", id=id.row.get("id")))
    elif "album" in uri:
        album = Spotify.get_album(spotify_id)
        if album:
            print("loading album")
            SQLLoader.loadAlbum(album)
            id = DB.selectOne("SELECT id FROM IS601_Albums WHERE album_id = %s", spotify_id)
            return redirect(url_for("albums.view", id=id.row.get("id")))
    elif "track" in uri:
        track = Spotify.get_track(spotify_id)
        if track:
            print("loading track")
            SQLLoader.loadTrack(track)
            id = DB.selectOne("SELECT id FROM IS601_Tracks WHERE track_id = %s", spotify_id)
            return redirect(url_for("tracks.view", id=id.row.get("id")))
    return redirect(url_for("root.index"))    

@root.route("/")
def index():
    tracks_info = []
    try:
        tracks_info = DB.select("""
            SELECT * 
            FROM IS601_Tracks 
            ORDER BY RAND()
            LIMIT 10
            """)
    except Exception as e:
        flash(f"Error fetching tracks: {e}", "danger")
    return render_template("index.html", tracks_info=tracks_info.rows)

@root.route("/search", methods=["GET"])
def search():
    # rk868 12/12/23 - Added search form
    form = SearchForm()
    #print("searching")
    try:
        if form.validate_on_submit():
            print("searching")
            try:
                if not form.limit.data:
                    form.limit.data = 20
                if form.query.data < 1 or form.query.data > 50:
                    flash("Limit must be between 1 and 50", "warning")
                    return render_template("search_page.html", form=form)

                result = Spotify.search(form.query.data, numberOfTopResults=form.limit.data)
                if result:
                    return render_template("search_page.html", form=form, top_results=result)
            except Exception as e:
                flash(f"Error searching for tracks: {e}", "danger")
        else:
            query = request.args.get("query")
            result = Spotify.search(query)
            print("result", type(result), result)
            if result:
                return render_template("search_page.html", form=form, top_results=result)
            else:
                flash(f"No results found for {query}", "warning")
    except Exception as e:
        flash(f"Error performing search: {e}", "danger")
        
    return render_template("search_page.html", form=form)

@root.route("/redirect", methods=["GET"])
def redirecter():
    uri = request.args.get("uri")
    if uri:
        id = checker(uri)
        if id:
            return redirect(url_for(f"{uri.split(':')[-2]}.view", id=id))
        else: 
            return api_call(uri)
    return redirect(url_for("root.index"))    