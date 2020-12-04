import uuid

from flask import request, session


def check_token(fun):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            return {
                       "success": False,
                       "remark": "用户未登录",
                   }, 401

        user_id = session.get(token)

        if not user_id:
            return {
                       "success": False,
                       "remark": "用户未登录",
                   }, 401

        fun(*args, *kwargs)

    return wrapper


def generate_token(prefix=None):
    token = prefix + uuid.uuid4().hex
    return token

