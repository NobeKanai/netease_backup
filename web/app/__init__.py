from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()


def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.from_object(config)

    # init db
    db.init_app(app)

    # init cors
    cors.init_app(app)

    from .api import bp
    app.register_blueprint(bp)

    return app
