from flask import request
from flask_restx import Resource, Namespace

from app.container import user_service
from app.dao.models.user import UserSchema
from app.utils import admin_required, auth_required

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/<username>")
class UserViews(Resource):

    @admin_required
    def get(self, username):
        user = user_service.get_one(username)
        return user_schema.dump(user), 200

    @admin_required
    def delete(self, username):
        user_service.delete_user(username)
        return 'Пользователь удален', 200

    @auth_required
    def put(self, username):
        req_json = request.json
        user_service.update_user(req_json, username)
        return 'пользователь обновлен', 201


@user_ns.route("/")
class UserViews(Resource):
    def get(self):
        users = user_service.get_all()
        return users_schema.dump(users)


    def post(self):
        data = request.json
        user_service.create_user(data)
        return 'Пользователь добавлен', 201




