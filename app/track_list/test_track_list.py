from app.track_list.getter import get_json, get_trackIds


def test_get():
    r_json = get_json(base_url="http://localhost:3000", playlist_id=751269939)
    assert r_json != ""


def test_get_trackIds():
    r_json = get_json(base_url="http://localhost:3000", playlist_id=751269939)
    l = get_trackIds(r_json)
    assert isinstance(l, list)
    assert len(l) != 0
