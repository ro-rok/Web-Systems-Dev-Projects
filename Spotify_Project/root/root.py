from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from root.forms import SearchForm
from utils.Spotify import Spotify
from utils.SQLLoader import SQLLoader

root = Blueprint('root', __name__, url_prefix='', template_folder='templates')

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
    form = SearchForm()
    #print("searching")
    if form.validate_on_submit():
        print("searching")
        try:
            if not form.limit.data:
                form.limit.data = 10
            if not form.offset.data:
                form.offset.data = 0
            if not form.type.data:
                form.type.data = "multi"
            result = Spotify.search(form.query.data, form.type.data, form.offset.data, form.limit.data)
            if result:
                if form.type.data == "track":
                    return render_template("tracks_search.html", form=form, tracks=result["tracks"])
                elif form.type.data == "artist":
                    return render_template("artists_search.html", form=form, artists=result["artists"])
                elif form.type.data == "album":
                    return render_template("albums_search.html", form=form, albums=result["albums"])
                else:
                    print(result)
                    return render_template("search.html", form=form, albums=result["albums"], artists=result["artists"], tracks=result["tracks"], top_results=result["top_results"])           
        except Exception as e:
            flash(f"Error searching for tracks: {e}", "danger")
    else:
        query = request.args.get("query")
        print(query)
        print(type(query))
        try:
            result = Spotify.search(query)
            print(result)
            if result:
                return render_template("search.html", form=form, albums=result["albums"], artists=result["artists"], tracks=result["tracks"], top_results=result["top_results"])
            else:
                flash(f"No results found for {query}", "warning")
        except Exception as e:
            flash(f"Error searching for {query}: {e}", "danger")
        
    return render_template("tracks_search.html", form=form)
