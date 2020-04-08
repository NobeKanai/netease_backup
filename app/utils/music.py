from .track_list import get_json, get_trackIds
from .track_detail import get_by_ids


def get_playlist(base_url, playlist_id):
    """ 获取歌单所有的id， 并不包括详情, id为int类型 """
    r_json = get_json(base_url, playlist_id)
    ids = get_trackIds(r_json)
    return ids


def get_all_songs(base_url, playlist_ids, request_len=5):
    """ 通过playlist_ids获取所有歌曲"""
    num = 0
    length = len(playlist_ids)
    res = []
    while num < length:
        if num + request_len < length:
            ids = playlist_ids[num:num + request_len]
        else:
            ids = playlist_ids[num:]

        res.extend(get_by_ids(baseURL=base_url, ids=ids))
        num += request_len
    return res
