from track_list import get_json, get_trackIds
from track_detail import get_by_ids

class PlayListQuery:
    def __init__(self, base_url="http://localhost:3000"):
        self.base_url = base_url
        self.playlist_ids = []

    def get_playlist(self, playlist_id):
        r_json = get_json(self.base_url, playlist_id)
        ids = get_trackIds(r_json)
        self.playlist_ids = ids
        return ids

    def get_all_songs(self, playlist_id=None, request_len=5):
        if playlist_id is None and self.playlist_ids == []:
            raise ValueError("您一次都没有提供过Playlist id")
        elif not self.playlist_ids:
            self.get_playlist(playlist_id)

        num = 0
        lenght = len(self.playlist_ids)
        res = []
        while num < lenght:
            if num + request_len < lenght:
                ids = self.playlist_ids[num:num + request_len]
            else:
                ids = self.playlist_ids[num:]

            res.extend(get_by_ids(baseURL=self.base_url, ids=ids))
            num += request_len
        return res
