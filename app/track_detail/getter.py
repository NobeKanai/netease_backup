import requests

GET_TRACK_DETAIL = "/song/detail"


def get_by_ids(baseURL, ids):
    """
    baseURL string
    ids     list[str]

    return the json data (list)
    """
    url = baseURL + GET_TRACK_DETAIL
    params = {"ids": ','.join(ids)}
    r = requests.get(url, params=params)
    try:
        data = r.json()
        return data["songs"]
    except ValueError:
        return None
