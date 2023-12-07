from utils.api import API

class Spotify(API):

    @staticmethod
    def get_track(track_id):
        query ={"ids": track_id}
        url = "/tracks/"
        results = API.get(url, query)
        return results
    
    @staticmethod
    def get_artist(artist_id):
        query ={"ids": artist_id}
        url = "/artists/"
        results = API.get(url, query)
        return results
    
    @staticmethod
    def get_album(album_id):
        query ={"id": album_id}
        url = "/albums/"
        results = API.get(url, query)
        return results
    
    @staticmethod
    def search(query, q_type="multi", offset=0, limit=30, numberOfTopResults=10):
        query = {"q": query, "type": q_type, "offset": offset, "limit": limit, "numberOfTopResults": numberOfTopResults}
