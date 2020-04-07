from app.track_detail.getter import get_by_ids
from app import PlayListQuery

playlist_id = input("playlist id:")

q = PlayListQuery()
all_song_list = q.get_all_songs(playlist_id)

for song in all_song_list:
    print("Name: ", song["name"])
    print("Author: ", ",".join([ar["name"] for ar in song["ar"]]))

print("\nthe len of all song is", len(all_song_list))
