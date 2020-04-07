from dotenv import load_dotenv
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, ".env"))


class Config:
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(base_dir, "app.db")
