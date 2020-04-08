# test models and database connection
from models import Track, get_session


def test_save_model():
    with get_session() as s:
        track = Track(id=1, name="music name", author="music author")
        s.add(track)
        s.commit()

        t = s.query(Track).filter(Track.id == 1).first()
        assert t.id == 1
        assert t.name == "music name"
        assert t.author == "music author"

        s.query(Track).filter(Track.id == 1).delete()
        s.commit()
