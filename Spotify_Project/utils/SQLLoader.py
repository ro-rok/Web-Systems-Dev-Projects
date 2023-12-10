from sql.db import DB
from flask import flash

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
                flash(f"Error creating album record: {e}", "danger")
            for artist in track["artists"]:
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                VALUES (%s, %s, %s)
                                """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                except Exception as e:
                    flash(f"Error creating artist record: {e}", "danger")
            try:
                DB.insertOne("""
                            INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, track_number, track_uri, track_img, duration_ms, is_explicit, release_date)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, track["track_id"], track["album"]["album_id"], track["track_name"], track["track_popularity"], track["track_number"], track["track_uri"], track["track_img"], track["duration_ms"], track["is_explicit"], track["release_date"])
            except Exception as e:
                flash(f"Error creating track record: {e}", "danger")
            try:
                DB.insertOne("""
                            INSERT INTO IS601_ArtistAlbum (artist_id, album_id)
                            VALUES (%s, %s)
                            """, artist["artist_id"], track["album"]["album_id"])
            except Exception as e:
                flash(f"Error creating artist album record: {e}", "danger")
        
    @staticmethod
    def loadAlbumsSearch(result):
        for album in result["albums"]:
            """if "albums" in results and results["albums"]["totalCount"] > 0:
            for items in results["albums"]["items"]:
                album = {}
                album["album_id"] = items["data"]["id"]
                album["album_name"] = items["data"]["name"]
                album["album_uri"] = items["data"]["uri"]
                album["album_img"] = Spotify.highest_height_cover(items["data"]["coverArt"]["sources"])
                release_date = "".join(items["data"]["date"].values())
                album["release_date"] = Spotify.convert_to_datetime(release_date)

                album_artist = {}
                album_artist["artist_id"] = items["data"]["artists"]["items"][0]["uri"].split(":")[2]
                album_artist["artist_name"] = items["data"]["artists"]["items"][0]["profile"]["name"]
                album_artist["artist_uri"] = items["data"]["artists"]["items"][0]["uri"]
                album["artist"] = album_artist
                albums.append(album)"""
            
            for album in result["albums"]:
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_Albums (album_id, album_name, album_uri, album_img, release_date)
                                VALUES (%s, %s, %s, %s, %s)
                                """, album["album_id"], album["album_name"], album["album_uri"], album["album_img"], album["release_date"])
                except Exception as e:
                    flash(f"Error creating album record: {e}", "danger")
                for artist in album["artists"]:
                    try:
                        DB.insertOne("""
                                    INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                    VALUES (%s, %s, %s)
                                    """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                    except Exception as e:
                        flash(f"Error creating artist record: {e}", "danger")
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_ArtistAlbum (artist_id, album_id)
                                VALUES (%s, %s)
                                """, artist["artist_id"], album["album_id"])
                except Exception as e:
                    flash(f"Error creating artist album record: {e}", "danger")

    @staticmethod
    def loadAristsSearch(result):
        """if "artists" in results and results["artists"]["totalCount"] > 0:
            for items in results["artists"]["items"]:
                artist = {}
                artist["artist_id"] = items["data"]["id"]
                artist["artist_name"] = items["data"]["profile"]["name"]
                artist["artist_uri"] = items["data"]["uri"]
                artist["artist_img"] = Spotify.highest_height_cover(items["data"]["visuals"]["avatarImage"]["sources"])
                artists.append(artist)     """
        for artist in result["artists"]:
            try:
                DB.insertOne("""
                            INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri, artist_img)
                            VALUES (%s, %s, %s, %s)
                            """, artist["artist_id"], artist["artist_name"], artist["artist_uri"], artist["artist_img"])
            except Exception as e:
                flash(f"Error creating artist record: {e}", "danger")

    @staticmethod
    def loadArtist(results):
        for result in results:
            """CREATE TABLE
                IS601_Artists (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    artist_id VARCHAR(50) UNIQUE NOT NULL,
                    artist_name VARCHAR(255) NOT NULL CHECK (artist_name <> ''),
                    artist_popularity INT CHECK (artist_popularity >= 0 AND artist_popularity <= 100) DEFAULT 0,
                    followers_total INT CHECK (followers_total >= 0),
                    artist_uri VARCHAR(100) CHECK (artist_uri <> ''),
                    artist_img VARCHAR(255) CHECK (artist_img <> ''),
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    UNIQUE KEY (artist_id)
                );"""
            try:
                DB.insertOne("""
                            INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri, artist_img, followers_total, artist_popularity)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                            artist_name = VALUES(artist_name),
                            artist_uri = VALUES(artist_uri),
                            artist_img = VALUES(artist_img),
                            followers_total = VALUES(followers_total),
                            artist_popularity = VALUES(artist_popularity)
                            """, result["artist_id"], result["artist_name"], result["artist_uri"], result["artist_img"], result["followers_total"], result["artist_popularity"])
                DB.insertOne("""
                            INSERT INTO IS601_Genres (genre_name) VALUES (%s)           
                            """, result["genre_name"])
                genre_id = DB.selectOne("""
                            SELECT id FROM IS601_Genres WHERE genre_name = %s
                            """, result["genre_name"])
                DB.insertOne(""" INSERT INTO IS601_ArtistGenre (artist_id, genre_id) VALUES (%s, %s) """, result["artist_id"], genre_id)
            except Exception as e:
                flash(f"Error creating/updating artist record: {e}", "danger")
    
    @staticmethod
    def loadAlbum(results):
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
                    DB.insertOne("""
                                INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                VALUES (%s, %s, %s)
                                """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                    DB.insertOne("""
                                INSERT INTO IS601_ArtistAlbum (artist_id, album_id)
                                VALUES (%s, %s)
                                """, artist["artist_id"], results["album_id"])
                except Exception as e:
                    flash(f"Error creating artist record: {e}", "danger")
            for track in results["tracks"]:
                try:
                    DB.insertOne("""
                                INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, track_number, track_uri, track_img, duration_ms, is_explicit, release_date, preview_url)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """, track["track_id"], results["album_id"], track["track_name"], track["track_popularity"], track["track_number"], 
                                    track["track_uri"], track["track_img"], track["duration_ms"], track["is_explicit"], results["release_date"], track["preview_url"])
                except Exception as e:
                    flash(f"Error creating track record: {e}", "danger")
                for artist in track["artists"]:
                    if artist["artist_id"] not in [s["artist_id"] for s in results["artists"]]:
                        try:
                            DB.insertOne("""
                                        INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri)
                                        VALUES (%s, %s, %s)
                                        """, artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                            DB.insertOne("""
                                        INSERT INTO IS601_ArtistTracks (track_id, artist_id)
                                        VALUES (%s, %s)
                                        """, track["track_id"], artist["artist_id"])
                        except Exception as e:
                            flash(f"Error creating artist record: {e}", "danger")
        except Exception as e:
            flash(f"Error creating/updating album record: {e}", "danger")
        
    @staticmethod
    def loadTrack(results):
        for track in results:
            try:
                DB.insertOne("INSERT INTO IS601_Albums (album_id, album_name, album_uri, album_img, release_date, total_tracks) VALUES (%s, %s, %s, %s, %s, %s)"
                            , track["album"]["album_id"], track["album"]["album_name"], track["album"]["album_uri"], track["album"]["album_img"], track["album"]["release_date"], track["album"]["total_tracks"])
                for artist in track["album"]["artists"]:
                    DB.insertOne("INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri) VALUES (%s, %s, %s)"
                                , artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                    DB.insertOne("INSERT INTO IS601_ArtistAlbum (artist_id, album_id) VALUES (%s, %s)"
                                , artist["artist_id"], track["album"]["album_id"])
            except Exception as e:
                flash(f"Error creating/updating album record: {e}", "danger")
            try:
                DB.insertOne("""INSERT INTO IS601_Tracks (track_id, album_id, track_name, track_popularity, track_number, track_uri, track_img, duration_ms, is_explicit, release_date, preview_url) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                for artist in track["artists"]:
                    if artist["artist_id"] not in [s["artist_id"] for s in track["album"]["artists"]]:
                        DB.insertOne("INSERT INTO IS601_Artists (artist_id, artist_name, artist_uri) VALUES (%s, %s, %s)"
                                    , artist["artist_id"], artist["artist_name"], artist["artist_uri"])
                        DB.insertOne("INSERT INTO IS601_ArtistTracks (track_id, artist_id) VALUES (%s, %s)"
                                    , track["track_id"], artist["artist_id"])
            except Exception as e:
                flash(f"Error creating/updating track record: {e}", "danger")
