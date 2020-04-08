from utils.music import get_playlist
from config import Config
import click
import time
from models import get_session, Track

playlist_temp = []


def compare_list(l1, l2):
    new_list = [i for i in l1 if i not in l2]
    return new_list


def start_loop(playlist_id, callback=None):
    """
    callback 接受一个vet参数， 保存新增的的歌曲id的列表
    """
    global playlist_temp

    playlist_ids = get_playlist(Config.BASE_URL, playlist_id)
    ret = compare_list(playlist_ids, playlist_temp)

    if ret:
        print("[PLAYLIST CHANGE], add follow songs' id to list:", "".join(ret))
        if callback:
            callback(ret)

    # 更新playlist_temp
    playlist_temp = playlist_ids


def init_playlist():
    global playlist_temp
    with get_session() as s:
        playlist_temp = [t.id for t in s.query(Track).all()]


@click.command()
@click.option("-id", "--playlist_id", help="歌单id", type=str)
def main(playlist_id):
    init_playlist()
    global playlist_temp

    print("Starting cycle....")
    while True:
        time.sleep(3600)
        start_loop(playlist_id)


if __name__ == '__main__':
    main()
