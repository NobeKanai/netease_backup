from .getter import get_by_ids


def test_get_by_ids():
    r1 = get_by_ids("http://localhost:3000", [347230, 484721168])
    r2 = get_by_ids("http://localhost:3000", [
        484721168,
    ])
    assert r1 and r2
