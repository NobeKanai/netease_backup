# generate model by sqlacodegen ... --flask
from sqlalchemy import BigInteger, Column, String
from . import db


class Track(db.Model):
    __tablename__ = 'track'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(128))
    author = db.Column(db.String(128))
    album = db.Column(db.String(128))

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "author": self.author.split("/"),
            "album": self.album
        }

        return data
