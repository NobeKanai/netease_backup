from utils.music import get_all_songs, get_playlist

base_url = "http://localhost:3000"


def test_get_all_songs():
    playlist = get_playlist(base_url, playlist_id="894748986")
    song_list = get_all_songs(base_url, playlist)
    print(song_list)
    assert isinstance(song_list, list)
    assert len(song_list) == 47  # 一段时间内不会变更的歌单长度
