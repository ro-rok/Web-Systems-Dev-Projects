import os
# fix for testing just this file
if __name__ == "__main__":
    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)



from utils.api import API

class RateLimitExceeded(Exception):
    """Thrown when the rate limit is throttled (not related to the overall quota)"""
    pass

from utils.api import API
from datetime import datetime

class Spotify(API):

    @staticmethod
    def get_track(track_id):
        #rk868 - 12/09/23 - This is the get function for tracks.
        query ={"ids": track_id}
        url = "/tracks/"
        results = API.get(url, query)
        print(results)
        import json
        with open("results.json", "w") as json_file:
            json.dump(results, json_file)
        if results : return Spotify.track_formatter(results)
        return results
    
    @staticmethod
    def get_artist(artist_id):
        #rk868 - 12/09/23 - This is the get function for artists.
        query ={"ids": artist_id}
        url = "/artists/"
        results = API.get(url, query)
        if results : return Spotify.artist_formatter(results)
        return results
    
    @staticmethod
    def get_album(album_id):
        #rk868 - 12/09/23 - This is the get function for albums.
        query ={"id": album_id}
        url = "/albums/"
        results = API.get(url, query)
        if results : return Spotify.album_formatter(results)
        return results
    
    @staticmethod
    def search(query, q_type="multi", offset=0, limit=30, numberOfTopResults=10):
        #rk868 - 12/09/23 - This is the search function for Spotify.
        query = {"q": query, "type": q_type, "offset": offset, "limit": limit, "numberOfTopResults": numberOfTopResults}
        url = "/search/"
        results = API.get(url, query)
        if results : return Spotify.search_formatter(results)
        return results

    @staticmethod
    def highest_height_cover(cover_url):
        #rk868 - 12/09/23 - This is the highest_height_cover function for Spotify.
        return max(cover_url, key=lambda cover: cover["height"])["url"]
        
    @staticmethod
    def convert_to_datetime(input_str):
        #rk868 - 12/09/23 - This is the convert_to_datetime function for Spotify.
        try:
            dt = datetime.strptime(input_str, '%Y-%m-%d')
        except ValueError:
            try:
                dt = datetime.strptime(input_str, '%Y-%m')
            except ValueError:
                try:
                    dt = datetime.strptime(input_str, '%Y')
                except ValueError:
                    raise ValueError("Invalid date format")
        return dt

    @staticmethod
    def search_formatter(results):
        #rk868 - 12/09/23 - This is the search_formatter function for Spotify.
        tracks = []
        artists = []
        albums = []
        top_results = []

        if "tracks" in results and results["tracks"]["totalCount"] > 0:
            for items in results["tracks"]["items"]:
                track = {}
                track["track_id"] = items["data"]["id"]
                track["album_id"] = items["data"]["albumOfTrack"]["id"]
                track["track_name"] = items["data"]["name"]
                track["track_popularity"] = items["data"]["popularity"]
                track["track_number"] = items["data"]["trackNumber"]
                track["track_uri"] = items["data"]["uri"]
                track["track_img"] = Spotify.highest_height_cover(items["data"]["coverArt"]["sources"])
                track["duration_ms"] = items["data"]["duration"]["totalMilliseconds"]
                track["is_explicit"] = items["data"]["contentRating"]["label"] == "EXPLICIT"
                release_date = "".join(items["data"]["albumOfTrack"]["date"].values())
                track["release_date"] = Spotify.convert_to_datetime(release_date)

                album = {}
                album["album_id"] = items["data"]["albumOfTrack"]["id"]
                album["album_name"] = items["data"]["albumOfTrack"]["name"]
                album["album_uri"] = items["data"]["albumOfTrack"]["uri"]
                album["album_img"] =  Spotify.highest_height_cover(items["data"]["albumOfTrack"]["coverArt"]["sources"])
                album["release_date"] = Spotify.convert_to_datetime(release_date)   
                track["album"] = album

                track_artists = []
                for artist in items["data"]["artists"]["items"]:
                    artist = {}
                    artist["artist_id"] = artist["uri"].split(":")[2]
                    artist["artist_name"] = artist["profile"]["name"]
                    artist["artist_uri"] = artist["uri"]
                    track_artists.append(artist)
                track["artists"] = track_artists
                tracks.append(track)

        if "albums" in results and results["albums"]["totalCount"] > 0:
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
                albums.append(album)

        if "artists" in results and results["artists"]["totalCount"] > 0:
            for items in results["artists"]["items"]:
                artist = {}
                artist["artist_id"] = items["data"]["id"]
                artist["artist_name"] = items["data"]["profile"]["name"]
                artist["artist_uri"] = items["data"]["uri"]
                artist["artist_img"] = Spotify.highest_height_cover(items["data"]["visuals"]["avatarImage"]["sources"])
                artists.append(artist)

        if "topResults" in results and results["topResults"]["items"]:
            for items in results["topResults"]["items"]:
                top_result = {}
                if "albumOfTrack" in items["data"]:
                    top_result["album_id"] = items["data"]["albumOfTrack"]["id"]
                    top_result["album_name"] = items["data"]["albumOfTrack"]["name"]
                    top_result["album_uri"] = items["data"]["albumOfTrack"]["uri"]
                    top_result["album_img"] = Spotify.highest_height_cover(items["data"]["albumOfTrack"]["coverArt"]["sources"])
                    release_date = "".join(items["data"]["albumOfTrack"]["date"].values())
                    top_result["release_date"] = Spotify.convert_to_datetime(release_date)
                    
                if "artists" in items["data"]:
                    top_result["artist_id"] = items["data"]["artists"]["items"][0]["uri"].split(":")[2]
                    top_result["artist_name"] = items["data"]["artists"]["items"][0]["profile"]["name"]
                    top_result["artist_uri"] = items["data"]["artists"]["items"][0]["uri"]
                    top_result["artist_img"] = Spotify.highest_height_cover(items["data"]["visuals"]["avatarImage"]["sources"])
                if "name" in items["data"]:
                    top_result["track_name"] = items["data"]["name"]
                    top_result["track_id"] = items["data"]["id"]
                    top_result["track_uri"] = items["data"]["uri"]
                    top_result["track_img"] = Spotify.highest_height_cover(items["data"]["coverArt"]["sources"])
                    top_result["track_popularity"] = items["data"]["popularity"]
                    top_result["track_number"] = items["data"]["trackNumber"]
                    top_result["duration_ms"] = items["data"]["duration"]["totalMilliseconds"]
                    top_result["is_explicit"] = items["data"]["contentRating"]["label"] == "EXPLICIT"
                    release_date = "".join(items["data"]["albumOfTrack"]["date"].values())
                    top_result["release_date"] = Spotify.convert_to_datetime(release_date)
                top_results.append(top_result)
        
        return {"tracks": tracks, "artists": artists, "albums": albums, "top_results": top_results}

    @staticmethod
    def album_formatter(results):
        #rk868 - 12/09/23 - This is the album_formatter function for Spotify.
        album = {}
        if "albums" in results:
            album["album_id"] = results["albums"][0]["id"]
            album["album_name"] = results["albums"][0]["name"]
            album["album_popularity"] = results["albums"][0]["popularity"]
            album["album_uri"] = results["albums"][0]["uri"]
            album["album_img"] = Spotify.highest_height_cover(results["albums"][0]["images"])
            album["total_tracks"] = results["albums"][0]["total_tracks"]
            album["release_date"] = Spotify.convert_to_datetime(results["albums"][0]["release_date"])
            album["label_name"] = results["albums"][0]["label"]
            
            album["artists"] = []
            for artist in results["albums"][0]["artists"]:
                album_artist = {}
                album_artist["artist_id"] = artist["id"]
                album_artist["artist_name"] = artist["name"]
                album_artist["artist_uri"] = artist["uri"]
                album["artists"].append(album_artist)
            
            album["tracks"] = []
            for track in results["albums"][0]["tracks"]["items"]:
                #print(track.keys())
                album_track = {}
                album_track["track_id"] = track["id"]
                album_track["track_name"] = track["name"]
                album_track["track_number"] = track["track_number"]
                album_track["track_uri"] = track["uri"]
                album_track["duration_ms"] = track["duration_ms"]
                album_track["is_explicit"] = track["explicit"]
                album_track["preview_url"] = track["preview_url"]
                album_track["track_popularity"] = results["albums"][0]["popularity"]
                album_track["track_img"] = Spotify.highest_height_cover(results["albums"][0]["images"])
                album_track["release_date"] = Spotify.convert_to_datetime(results["albums"][0]["release_date"])
                album_track["artists"] = []
                for artist in track["artists"]:
                    album_track_artist = {}
                    album_track_artist["artist_id"] = artist["id"]
                    album_track_artist["artist_name"] = artist["name"]
                    album_track_artist["artist_uri"] = artist["uri"]
                    album_track["artists"].append(album_track_artist)
                album["tracks"].append(album_track)
        #print(album.keys())
        return album
    
    @staticmethod
    def artist_formatter(results):
        #rk868 - 12/09/23 - This is the artist_formatter function for Spotify.
        artists = []
        if "artists" in results:
            #print(results["artists"][0].keys())
            for a in results["artists"]:
                if not a: continue
                artist = {}
                #print(artist.keys())
                artist["artist_id"] = a["id"]
                artist["artist_name"] = a["name"]
                artist["artist_uri"] = a["uri"]
                artist["artist_img"] = Spotify.highest_height_cover(a["images"])
                artist["genres"] = a["genres"]
                artist["followers_total"] = a["followers"]["total"]
                artist["artist_popularity"] = a["popularity"]
                artists.append(artist)
        return artists
    
    @staticmethod
    def track_formatter(results):
        #rk868 - 12/09/23 - This is the track_formatter function for Spotify.
        tracks = []
        if "tracks" in results:
            for t in results["tracks"]:
                if not t: continue
                track = {}
                track["track_id"] = t["id"]
                track["track_name"] = t["name"]
                track["track_popularity"] = t["popularity"]
                track["track_uri"] = t["uri"]
                track["is_explicit"] = t["explicit"]
                track["preview_url"] = t["preview_url"]
                track["track_number"] = t["track_number"]
                track["duration_ms"] = t["duration_ms"]
                track["track_img"] = Spotify.highest_height_cover(t["album"]["images"])
                track["release_date"] = Spotify.convert_to_datetime(t["album"]["release_date"])

                album = {}
                album["album_id"] = t["album"]["id"]
                album["album_name"] = t["album"]["name"]
                album["album_uri"] = t["album"]["uri"]
                album["album_img"] = Spotify.highest_height_cover(t["album"]["images"])
                album["release_date"] = Spotify.convert_to_datetime(t["album"]["release_date"])
                album["total_tracks"] = t["album"]["total_tracks"]
                album_artists = []
                for artist in t["album"]["artists"]:
                    album_artist = {}
                    album_artist["artist_id"] = artist["id"]
                    album_artist["artist_name"] = artist["name"]
                    album_artist["artist_uri"] = artist["uri"]
                    album_artists.append(album_artist)
                album["artists"] = album_artists

                track["album"] = album

                track_artists = []
                for artist in t["artists"]:
                    track_artist = {}
                    track_artist["artist_id"] = artist["id"]
                    track_artist["artist_name"] = artist["name"]
                    track_artist["artist_uri"] = artist["uri"]
                    track_artists.append(track_artist)
                
                track["artists"] = track_artists
                tracks.append(track)

        return tracks


if __name__ == "__main__":
    dir = r"utils\sample\tracks.json"
    
    import json
    with open(dir, "r") as f:
        results = json.load(f)
    print(results.keys())
    print(results.keys())
    r =Spotify.track_formatter(results)
    print(type(r))
    print(r[0].keys())

    print(r[0]["album"].keys())
    print(r[0]["album"])
    print(r[0]["album"]["artists"][0].keys())
    print(r[0]["album"]["artists"][0])
    print(r[0]["artists"][0].keys())

    print(r)