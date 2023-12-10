from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from root.forms import SearchForm
from utils.Spotify import Spotify
from utils.FormLoader import FormLoader

root = Blueprint('root', __name__, url_prefix='', template_folder='templates')

@root.route("/")
def index():
    try:
        tracks_info = DB.select("""
            SELECT * 
            FROM IS601_Tracks 
            ORDER BY RAND()
            LIMIT 10
            """)
    except Exception as e:
        flash(f"Error fetching tracks: {e}", "danger")
    return render_template("index.html" ,tracks_info=tracks_info)

@root.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        try:
            result = Spotify.search(form.query.data, form.type.data, form.offset.data, form.limit.data)
            if result:
                if form.type.data == "track":
                    return render_template("tracks_search.html", form=form, tracks=result["tracks"])
                elif form.type.data == "artist":
                    return render_template("artists_search.html", form=form, artists=result["artists"])
                elif form.type.data == "album":
                    return render_template("albums_search.html", form=form, albums=result["albums"])
                else:
                    return render_template("search.html", form=form, albums=result["albums"], artists=result["artists"], tracks=result["tracks"], top_results=result["top_results"])
        except Exception as e:
            flash(f"Error searching for tracks: {e}", "danger")
    return render_template("tracks_search.html", form=form)
