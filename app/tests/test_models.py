# test models and database connection
from models import Track, get_session
from main import on_add


def test_save_model():
    with get_session() as s:
        track = Track(id=1, name="music name", author="music author")
        s.add(track)
        s.commit()

        t = s.query(Track).filter(Track.id == 1).first()
        assert t.name == "music name"
        assert t.author == "music author"

        s.query(Track).filter(Track.id == 1).delete()
        s.commit()


def test_callback_func():
    vet = ["432486477"]
    on_add(vet)
    with get_session() as s:
        track = s.query(Track).filter(Track.id == 432486477).first()
        assert track.name == "ライアーダンス"
        assert track.author == "DECO*27/初音ミク"

        s.delete(track)
        s.commit()
