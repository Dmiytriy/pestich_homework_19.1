from flask import request
from flask_restx import Resource, Namespace

from app.container import user_service
from app.dao.models.user import UserSchema

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UserViews(Resource):
    def get(self):
        query = user_service.get_all()
        return users_schema.dump(query)

    def post(self):
        req_json = request.json
        user = user_service.create_user(req_json)
        return 'Пользователь добавлен', 201, {"location": f"/users/{user}"}


@user_ns.route("/<int:uid>")
class UserViews(Resource):
    def get(self, uid: int):
        query = user_service.get_one(uid)
        answer = user_schema.dump(query)

        if len(answer) == 0:
            return 'такого пользователя нет'

        return answer, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return '', 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204

