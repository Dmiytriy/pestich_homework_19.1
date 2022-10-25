from flask import Flask
from flask_restx import Api

from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns
from config import Config
from setup_db import db

def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):

    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    config = Config()
    app = create_app(config)

    app.run()
