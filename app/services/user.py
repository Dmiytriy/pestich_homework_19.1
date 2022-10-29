import base64
import hashlib
import hmac

import jwt
from app.constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.dao.user import UserDAO
from datetime import datetime, timedelta


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, user_name):
        return self.dao.get_one(user_name)

    def delete_user(self, user_name):
        self.dao.delete_user(user_name)

    def update_user(self, data, username):
        password = data.get('password')
        hashed_password = self.get_hash(password)
        data['password'] = hashed_password
        self.dao.update_user(data, username)

    def get_all(self):
        return self.dao.get_all()

    def create_user(self, data):
        password = data.get('password')
        hashed_password = self.get_hash(password)
        data['password'] = hashed_password
        self.dao.create_user(data)

    def get_hash(self, password):
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hashed_password)

    def compare_passwords(self, password_hash, other_password):

        decoder_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
            )

        return hmac.compare_digest(decoder_digest, hash_digest)



