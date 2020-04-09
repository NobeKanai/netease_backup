# test models and database connection
from models import Track, get_session
from main import on_add


def test_save_model():
    with get_session() as s:
        track = Track(id=1,
                      name="music name",
                      author="music author",
                      album="music album")
        s.add(track)
        s.commit()

        t = s.query(Track).filter(Track.id == 1).first()
        assert t.name == "music name"
        assert t.author == "music author"
        assert t.album == "music album"

        s.delete(t)
        s.commit()


def test_callback_func():
    vet = [714698]
    on_add(vet)
    with get_session() as s:
        track = s.query(Track).filter(Track.id == 714698).first()
        assert track.name == "冥界夜桜"
        assert track.author == "dBu music"

        s.delete(track)
        s.commit()
