from common.utils import JsonSerializable

class Artist(JsonSerializable):
    def __init__(self, artist_id, artist_name, artist_popularity, followers_total, artist_uri, artist_img):

        self.artist_id = artist_id
        self.artist_name = artist_name
        self.artist_popularity = artist_popularity
        self.followers_total = followers_total
        self.artist_uri = artist_uri
        self.artist_img = artist_img
        