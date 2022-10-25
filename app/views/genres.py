from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.models.genre import GenreSchema, Genre
from app.utils import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreViews(Resource):
    @auth_required
    def get(self):
        query = genre_service.get_genres()
        return genres_schema.dump(query)

    @admin_required
    def post(self):

        try:
            data = request.json
            genre_service.create(data)
            return '', 201
        except Exception:
            return 404


@genre_ns.route("/<int:gid>")
class GenreViews(Resource):
    @auth_required
    def get(self, gid: int):
        query = genre_service.get_genre(gid)
        answer = genre_schema.dump(query)

        if len(answer) == 0:
            return 'таких жанров нет'

        return answer, 200

    @admin_required
    def put(self, gid):

        try:
            data = request.json
            genre_service.update(data)
            return '', 201
        except Exception:
            return 404

    @admin_required
    def delete(self, gid):

        try:
            genre_service.delete(gid)
            return '', 201
        except Exception:
            return 404
