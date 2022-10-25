from flask import request
from flask_restx import Resource, Namespace, abort

from app.container import user_service
from app.dao.models.user import UserSchema

auth_ns = Namespace('auth')


@auth_ns.route("/")
class AuthViews(Resource):
    def post(self):
        req_json = request.json

        username = req_json.get('username')
        password = req_json.get('password')

        if not username and not password:
            abort(400)

        token = user_service.auth_user(username. username, password)

        if not token:
            return {"error": "Ошибка в логине или пароле"}, 401

        return token, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')

        if refresh_token in None:
            return {'error': 'Токен плохой'}, 400

        tokens = user_service.check_refresh_token(refresh_token)

        return tokens, 201



