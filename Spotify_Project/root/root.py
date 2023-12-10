from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB 
from roles.permissions import admin_permission
from root.forms import SearchForm
from utils.Spotify import Spotify

root = Blueprint('root', __name__, url_prefix='', template_folder='templates')

@root.route("/")
def index():
    try:
        tracks_info = DB.select("""
            SELECT * 
            FROM IS601_Tracks 
            WHERE track_id IN (
                SELECT track_id
                FROM IS601_Track_Artist
                WHERE artist_id IN (
                    SELECT artist_id
                    FROM IS601_Artists
                )
            ) AND track_id IN (
                SELECT track_id
                FROM IS601_Track_Album
                WHERE album_id IN (
                    SELECT album_id
                    FROM IS601_Albums
                )
            )
        """)
    except Exception as e:
        flash(f"Error fetching tracks: {e}", "danger")
    return render_template("index.html" ,tracks_info=tracks_info)

@root.route("/search", methods=["GET", "POST"])
def tracks():
    form = SearchForm()
    if form.validate_on_submit():
        try:
            pass
        except Exception as e:
            flash(f"Error searching for tracks: {e}", "danger")
    return render_template("tracks_search.html", form=form)
