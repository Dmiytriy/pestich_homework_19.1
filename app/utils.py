import jwt
from flask import request, abort
from constant import algo, secret


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception:
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            token_decoded = jwt.decode(token, secret, algorithms=[algo])
            if token_decoded['role'] != 'admin':
                abort(403)
        except Exception:
            abort(401)
        return func(*args, **kwargs)
    return wrapper
