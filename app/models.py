import contextlib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, BigInteger, String

from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base(engine)


@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


class Track(Base):
    __tablename__ = "track"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(64))
    author = Column(String(32))

    @classmethod
    def from_dict(cls, d):
        return cls(id=d["id"],
                   name=d["name"],
                   author=d.get("author")
                   or "/".join(map(lambda ar: ar["name"], d["ar"])))
