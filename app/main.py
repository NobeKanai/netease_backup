from utils.music import get_playlist, get_all_songs
from config import Config
import click
import time
from models import get_session, Track

playlist_temp = []


def on_add(ret):
    songs = get_all_songs(Config.BASE_URL, ret)
    with get_session() as s:
        for song in songs:
            t = Track.from_dict(song)
            s.add(t)
        s.commit()

    print("已全部提交至数据库")


def compare_list(l1, l2):
    s = set(l2)  # 使用set提升查找性能
    new_list = [i for i in l1 if i not in s]

    return new_list


def start_loop(playlist_id, callback=None):
    """
    callback 接受一个ret参数， 保存新增的的歌曲id的列表
    """
    global playlist_temp

    playlist_ids = get_playlist(Config.BASE_URL, playlist_id)
    ret = compare_list(playlist_ids, playlist_temp)

    if ret:
        print("[PLAYLIST CHANGE], add %d songs id to list:", len(ret))
        if callback:
            print("启动回调函数")
            callback(ret)

    # 更新playlist_temp
    playlist_temp = playlist_ids


def init_playlist():
    global playlist_temp
    with get_session() as s:
        playlist_temp = [
            t[0] for t in s.query(Track).with_entities(Track.id).all()
        ]


@click.command()
@click.option("-id", "--playlist_id", help="歌单id", type=str, required=True)
def main(playlist_id):

    init_playlist()
    global playlist_temp

    print("Starting cycle....")
    while True:
        start_loop(playlist_id, on_add)
        time.sleep(3600)


if __name__ == '__main__':
    main()
