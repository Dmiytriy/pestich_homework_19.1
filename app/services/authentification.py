import calendar
import datetime
from flask import abort
import jwt

from app.constant import secret, algo
from app.services.user import UserService


class AuthentificaionService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_one(username)


        if user is None:
            abort(401)

        if not is_refresh:

            if not self.user_service.compare_passwords(user.password, password):
                abort(401)

        data = {"username": user.username, "role": user.role}

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def update_tokens(self, token):
        try:
            user_data = jwt.decode(jwt=token, key=secret, algorithms=[algo])
            user_name = user_data.get('username')
            print(user_name)
            return self.generate_tokens(user_name, None, is_refresh=True)
        except Exception:
            abort(401)
