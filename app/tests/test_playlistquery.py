from app import PlayListQuery


def test_get_all_songs():
    p = PlayListQuery()
    song_list = p.get_all_songs(playlist_id="894748986")
    print(song_list)
    assert isinstance(song_list, list)
    assert len(song_list) == 47  # 一段时间内不会变更的歌单长度
