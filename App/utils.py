import uuid

from flask import request, session

def check_token(fun):
    def wrapper(*args, **kwargs):
        token = request.headers.get("token")

        user_id = get_user_id(token)

        if not user_id:
            return {
                       "success": False,
                       "remark": "用户未登录",
                   }, 401

        return fun(*args, *kwargs)

    return wrapper


def generate_token(prefix=''):
    token = prefix + uuid.uuid4().hex
    return token


def get_user_id(token):
    if token:
        return session.get(token) or ''
    return ''