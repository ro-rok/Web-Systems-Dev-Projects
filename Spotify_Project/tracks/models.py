from datetime import datetime
from common.utils import JsonSerializable


class Track(JsonSerializable):

    def __init__(self, track_id: str, album_id: str, track_name: str, track_popularity: int,
                 preview_url: str, track_number: int, track_uri: str, track_img: str,
                 duration_ms: int, is_explicit: bool, release_date: datetime,
                 created: datetime = None, modified: datetime = None):
        self.track_id = track_id
        self.album_id = album_id
        self.track_name = track_name
        self.track_popularity = track_popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.track_uri = track_uri
        self.track_img = track_img
        self.duration_ms = duration_ms
        self.is_explicit = is_explicit
        self.release_date = release_date
        self.created = created
        self.modified = modified