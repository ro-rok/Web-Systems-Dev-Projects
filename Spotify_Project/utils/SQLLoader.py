import os
# fix for testing just this file
if __name__ == "__main__":
    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)

from sql.db import DB
from flask import flash
from utils.Spotify import Spotify

class SQLLoader:
    @staticmethod
    def loadTracksSearch(result):
        for track in result["tracks"]:
            try:
                DB.insertOne("""
                            INSERT INTO IS601_Albums (album_id, album_name, album_uri, album_img, release_date)
                            VALUES (%s, %s, %s, %s, %s)
                            """, track["album"]["album_id"], track["album"]["album_name"], track["album"]["album_uri"], track["album"]["album_img"], track["album"]["release_date"])
            except Exception as e:
                if "Duplicate entry" in str(e):                print(f"Error creating album record: {e}", "danger")
                else:
                    flash(f"Error creating album record: {e}", "danger")
            for artist in track["artists"]:
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                VALUES (%s, %s, %s)
                                """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print(f"Error creating artist record: {e}", "danger")
                    else:
                        flash(f"Error creating artist record: {e}", "danger")
            try:
                DB.insertOne("""
                            INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, track_number, track_uri, track_img, duration_ms, is_explicit, release_date)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, track["track_id"], track["album"]["album_id"], track["track_name"], track["track_popularity"], track["track_number"], track["track_uri"], track["track_img"], track["duration_ms"], track["is_explicit"], track["release_date"])
            except Exception as e:
                if "Duplicate entry" in str(e):
                    print(f"Error creating track record: {e}", "danger")
                else:
                    flash(f"Error creating track record: {e}", "danger")
            try:
                DB.insertOne("""
                            INSERT INTO IS601_ArtistAlbums (artist_id, album_id)
                            VALUES (%s, %s)
                            """, artist["artist_id"], track["album"]["album_id"])
            except Exception as e:
                if "Duplicate entry" in str(e):
                    print(f"Error creating artist album record: {e}", "danger")
                else:
                    flash(f"Error creating artist album record: {e}", "danger")
        
    @staticmethod
    def loadAlbumsSearch(result):
        for album in result["albums"]:
            for album in result["albums"]:
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_Albums (album_id, album_name, album_uri, album_img, release_date)
                                VALUES (%s, %s, %s, %s, %s)
                                """, album["album_id"], album["album_name"], album["album_uri"], album["album_img"], album["release_date"])
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print(f"Error creating album record: {e}", "danger")
                    else:
                        flash(f"Error creating album record: {e}", "danger")
                for artist in album["artists"]:
                    try:
                        DB.insertOne("""
                                    INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                    VALUES (%s, %s, %s)
                                    """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                    except Exception as e:
                        if "Duplicate entry" in str(e):
                            print(f"Error creating artist record: {e}", "danger")
                        else:
                            flash(f"Error creating artist record: {e}", "danger")
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_ArtistAlbums (artist_id, album_id)
                                VALUES (%s, %s)
                                """, artist["artist_id"], album["album_id"])
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print(f"Error creating artist album record: {e}", "danger")
                    else:
                        flash(f"Error creating artist album record: {e}", "danger")

    @staticmethod
    def loadAristsSearch(result):

        for artist in result["artists"]:
            try:
                DB.insertOne("""
                            INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri, artist_img)
                            VALUES (%s, %s, %s, %s)
                            """, artist["artist_id"], artist["artist_name"], artist["artist_uri"], artist["artist_img"])
            except Exception as e:
                if "Duplicate entry" in str(e):
                    print(f"Error creating artist record: {e}", "danger")
                else:
                    flash(f"Error creating artist record: {e}", "danger")

    @staticmethod
    def loadArtist(results: list[dict]):
        for result in results:
            try:
                status = DB.insertOne("""
                            INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri, artist_img, followers_total, artist_popularity)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                            artist_name = VALUES(artist_name),
                            artist_uri = VALUES(artist_uri),
                            artist_img = VALUES(artist_img),
                            followers_total = VALUES(followers_total),
                            artist_popularity = VALUES(artist_popularity)
                            """, result["artist_id"], result["artist_name"], result["artist_uri"], result["artist_img"], result["followers_total"], result["artist_popularity"])
                print("status", status)
            except Exception as e:
                if "Duplicate entry" in str(e):
                    print(f"Error creating artist record: {e}", "danger")
                else:
                    flash(f"Error creating artist record: {e}", "danger")
            
            for genre in result["genres"]:
                print("genre", genre)
                try:
                    pass
                except Exception as e:
                    print(f"Error creating genre record: {e}", "danger")
                try:
                    genre_id = DB.selectOne(""" SELECT id FROM IS601_Genres WHERE genre_name = %s """, genre)
                    print("genre_id", genre_id.row.get("id"))
                    print("artist_id", result["artist_id"], result["artist_name"])
                    DB.insertOne(""" INSERT INTO IS601_ArtistGenres (artist_id, genre_id) VALUES (%s, %s) """, result["artist_id"], genre_id.row.get("id"))
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print(f"Error creating artist genre record: {e}", "danger")
                    else:
                        flash(f"Error creating artist genre record: {e}", "danger")
    
    @staticmethod
    def loadAlbum(results: dict):
        try:
            DB.insertOne("""
                        INSERT INTO IS601_Albums (album_id, album_name, album_uri, album_img, release_date, label_name, album_popularity, total_tracks)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        album_name = VALUES(album_name),
                        album_uri = VALUES(album_uri),
                        album_img = VALUES(album_img),
                        release_date = VALUES(release_date),
                        label_name = VALUES(label_name),
                        album_popularity = VALUES(album_popularity),
                        total_tracks = VALUES(total_tracks)
                        """, results["album_id"], results["album_name"], results["album_uri"], results["album_img"], results["release_date"], results["label_name"], results["album_popularity"], results["total_tracks"])
            for artist in results["artists"]:
                try:
                    try:
                        DB.insertOne("""
                                    INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                    VALUES (%s, %s, %s) 
                                    """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                    except Exception as e:
                        if "Duplicate entry" in str(e):
                            print(f"Error creating artist record: {e}", "danger")
                        else:
                            flash(f"Error creating artist record: {e}", "danger")

                    try:
                        DB.insertOne("""
                                    INSERT INTO IS601_ArtistAlbums (artist_id, album_id)
                                    VALUES (%s, %s)
                                    """, artist["artist_id"], results["album_id"])
                    except Exception as e:
                        if "Duplicate entry" in str(e):
                            print(f"Error creating artist record: {e}", "danger")
                        else:
                            flash(f"Error creating artist record: {e}", "danger")
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print(f"Error creating artist record: {e}", "danger")
                    else:
                        flash(f"Error creating artist record: {e}", "danger")
            for track in results["tracks"]:
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, track_number, track_uri, track_img, duration_ms, is_explicit, release_date, preview_url)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """, track["track_id"], results["album_id"], track["track_name"], track["track_popularity"], track["track_number"], 
                                    track["track_uri"], track["track_img"], track["duration_ms"], track["is_explicit"], results["release_date"], track["preview_url"])
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print(f"Error creating track record: {e}", "danger")
                    else:
                        flash(f"Error creating track record: {e}", "danger")
                for artist in track["artists"]:
                    if artist["artist_id"] not in [s["artist_id"] for s in results["artists"]]:
                        try:
                            DB.insertOne("""
                                        INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                        VALUES (%s, %s, %s)
                                        """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print(f"Error creating artist record: {e}", "danger")
                            else:
                                flash(f"Error creating artist record: {e}", "danger")
                        try:
                            DB.insertOne("""
                                        INSERT INTO IS601_TrackFeatures (track_id, artist_id)
                                        VALUES (%s, %s)
                                        """, track["track_id"], artist["artist_id"])
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print(f"Error creating artist record: {e}", "danger")
                            else:
                                flash(f"Error creating artist record: {e}", "danger")
        except Exception as e:
            if "Duplicate entry" in str(e):
                print(f"Error creating/updating album record: {e}", "danger")
            else:
                flash(f"Error creating/updating album record: {e}", "danger")
    @staticmethod
    def loadTrack(results : list[dict]):
        for track in results:
            try:
                DB.insertOne("INSERT INTO IS601_Albums (album_id, album_name, album_uri, album_img, release_date, total_tracks) VALUES (%s, %s, %s, %s, %s, %s)"
                            , track["album"]["album_id"], track["album"]["album_name"], track["album"]["album_uri"], track["album"]["album_img"], track["album"]["release_date"], track["album"]["total_tracks"])
            except Exception as e:
                if "Duplicate entry" in str(e):
                    print(f"Error creating/updating album record: {e}", "danger")
                else:
                    flash(f"Error creating/updating album record: {e}", "danger")
                for artist in track["album"]["artists"]:
                    try:
                        DB.insertOne("INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri) VALUES (%s, %s, %s)"
                                    , artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                    except Exception as e:
                        if "Duplicate entry" in str(e):
                            print(f"Error creating artist record: {e}", "danger")
                        else:
                            flash(f"Error creating artist record: {e}", "danger")
                    try:
                        DB.insertOne("INSERT INTO IS601_ArtistAlbums (artist_id, album_id) VALUES (%s, %s)"
                                    , artist["artist_id"], track["album"]["album_id"])
                    except Exception as e:
                        if "Duplicate entry" in str(e):
                            print(f"Error creating artist record: {e}", "danger")
                        else:
                            flash(f"Error creating artist record: {e}", "danger")
            try:
                DB.insertOne("""INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, track_number, track_uri, track_img, duration_ms, is_explicit, release_date, preview_url) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                track_name = VALUES(track_name),
                                track_popularity = VALUES(track_popularity),
                                track_number = VALUES(track_number),
                                track_uri = VALUES(track_uri),
                                track_img = VALUES(track_img),
                                duration_ms = VALUES(duration_ms),
                                is_explicit = VALUES(is_explicit),
                                release_date = VALUES(release_date),
                                preview_url = VALUES(preview_url)
                                """, track["track_id"], track["album"]["album_id"], track["track_name"], track["track_popularity"], track["track_number"], track["track_uri"], track["track_img"], 
                                    track["duration_ms"], track["is_explicit"], track["release_date"], track["preview_url"])
            except Exception as e:
                if "Duplicate entry" in str(e):
                    print(f"Error creating/updating track record: {e}", "danger")
                else:
                    flash(f"Error creating/updating track record: {e}", "danger")
                for artist in track["artists"]:
                    if artist["artist_id"] not in [album["artist_id"] for album in track["album"]["artists"]]:
                        try:
                            DB.insertOne("INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri) VALUES (%s, %s, %s)"
                                        , artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print(f"Error creating artist record: {e}", "danger")
                            else:
                                flash(f"Error creating artist record: {e}", "danger")
                        try:
                            DB.insertOne("INSERT INTO IS601_TrackFeatures (track_id, artist_id) VALUES (%s, %s)"
                                        , track["track_id"], artist["artist_id"])
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print(f"Error creating artist track record: {e}", "danger")
                            else:
                                flash(f"Error creating artist track record: {e}", "danger")

if __name__ == "__main__":
    dir = r"utils\track.json"
    

    import json
    with open(dir, "r") as f:
        results = json.load(f)
    r =Spotify.track_formatter(results)
    r = SQLLoader.loadTrack(r)
    print(r)