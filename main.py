from app import PlayListQuery
import click


@click.command()
@click.option("-id", "--playlist_id", help="歌单id", type=str)
def main(playlist_id):
    q = PlayListQuery()
    all_song_list = q.get_all_songs(playlist_id)

    for song in all_song_list:
        print("Name: ", song["name"])
        print("Author: ", ",".join([ar["name"] for ar in song["ar"]]))

    print("\nthe len of all song is", len(all_song_list))


if __name__ == '__main__':
    main()
