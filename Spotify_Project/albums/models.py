from common.utils import JsonSerializable
from datetime import datetime


class Album(JsonSerializable):

    def __init__(self, album_id: str, album_name: str, album_type: str, album_popularity: int, album_uri: str, album_img: str, total_track:int, release_date: datetime):
        self.album_id = album_id
        self.album_name = album_name
        self.album_type = album_type
        self.album_popularity = album_popularity
        self.album_uri = album_uri
        self.album_img = album_img
        self.total_track = total_track
        self.release_date = release_date