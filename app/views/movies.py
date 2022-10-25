from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.models.movie import MovieSchema, Movie
from app.utils import admin_required, auth_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieViews(Resource):
    @auth_required
    def get(self):
        all_movies = movie_service.get_all()

        if director_id := request.args.get('director_id'):
            all_movies = movie_service.get_by_director(director_id)

        if genre_id := request.args.get('genre_id'):
            all_movies = movie_service.get_by_genre(genre_id)

        if year := request.args.get('year'):
            all_movies = movie_service.get_by_year(year)

        answer = movies_schema.dump(all_movies)

        if len(answer) == 0:
            return 'таких фильмов нет'

        return answer, 200

    @admin_required
    def post(self):
        try:
            data = request.json
            movie_service.create_movie(data)
            return 'Данные внесены', 201
        except Exception as e:
            return f'{e}', 404


@movie_ns.route("/<int:mid>")
class MovieViews(Resource):
    @auth_required
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        answer = movie_schema.dump(movie)

        if len(answer) == 0:
            return 'таких фильмов нет'

        return answer, 200

    @admin_required
    def put(self, mid):
        try:
            data = request.json
            data["id"] = mid
            movie_service.update(data)
            return 'Данные изменены', 201
        except Exception as e:
            return f'{e}', 404

    @admin_required
    def delete(self, mid: int):
        try:
            movie_service.delete(mid)
            return 'Данные удалены', 201
        except Exception as e:
            return e, 404
