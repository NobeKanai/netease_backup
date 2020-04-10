import requests
from config import Config



def get_by_ids(baseURL, ids):
    """
    baseURL string
    ids     list[str]

    return the json data (list)
    """
    url = baseURL + Config.TRACK_DETAIL_API
    params = {"ids": ','.join([str(i) for i in ids])}
    r = requests.get(url, params=params)
    try:
        data = r.json()
        return data["songs"]
    except ValueError:
        return None
