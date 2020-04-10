from dotenv import load_dotenv
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, ".env"))


class Config:
    BASE_URL = "http://localhost:3000"  # api地址
    SQLALCHEMY_DATABASE_URL = os.environ.get(
        "DATABASE_URL") or "sqlite:///" + os.path.join(base_dir, "app.db")

    PLAYLIST_GET_API = os.environ.get(
        "PLAYLIST_GET_API") or "/playlist/detail"  # api 获取歌单全部歌曲id
    TRACK_DETAIL_API = os.environ.get(
        "TRACK_DETAIL_API") or "/song/detail"  # api 获取音乐详情
