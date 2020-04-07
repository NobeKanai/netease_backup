import requests

PLAYLIST_GETT_API = "/playlist/detail"


def get_json(base_url, playlist_id):
    """
    get_json 返回一个 json格式数据(字典), 包含从api返回的全部数据
    """
    url = base_url + PLAYLIST_GETT_API
    r = requests.get(url, params={"id": playlist_id})
    try:
        data = r.json()
        return data
    except ValueError:
        return ""


def get_trackIds(data):
    """
    get_trackIds 接受一个字典， 从字典内部返回所有歌曲Id的列表
    注意返回的ids为字符串格式
    """
    l = []
    for trackId in data["playlist"]["trackIds"]:
        l.append(str(trackId["id"]))  # 保存的id为字符串格式
    return l
