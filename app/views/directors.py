from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.models.director import DirectorSchema
from app.utils import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorViews(Resource):
    @auth_required
    def get(self):
        query = director_service.get_directors()
        return directors_schema.dump(query)

    @admin_required
    def post(self):

        try:
            data = request.json
            director_service.create(data)
            return '', 201
        except Exception:
            return 404


@director_ns.route("/<int:did>")
class DirectorViews(Resource):
    @auth_required
    def get(self, did):
        query = director_service.get_director(did)
        answer = director_schema.dump(query)

        if len(answer) == 0:
            return 'таких режиссеров нет'

        return answer, 200

    @admin_required
    def put(self):

        try:
            data = request.json
            director_service.update(data)
            return '', 201
        except Exception:
            return  404

    @admin_required
    def delete(self, did):

        try:
            director_service.delete(did)
            return '', 201
        except Exception:
            return 404

