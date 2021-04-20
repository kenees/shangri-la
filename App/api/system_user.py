import time
from flask import request, session
from flask_restful import Resource, fields, marshal, reqparse
from App.models import SystemUser
from App.utils import generate_token

user_fields = {
    "user_id": fields.Integer(),
    "user_avatar": fields.String,
    "user_name": fields.String,
    "authority": fields.String,
}

# 输入过滤
parser = reqparse.RequestParser()
parser.add_argument("user_name")
parser.add_argument("password")
parser.add_argument("token", location="headers")

class UserRegister(Resource):

    def post(self):
        args = parser.parse_args()
        user_name = args.get('user_name')
        password = args.get('password')
        system_user = SystemUser()

        try:
            system_user.user_name = user_name
            system_user.password = password
            system_user.create_at = int(time.time())
            system_user.save()
        except:
            return {
                "remark": "注册失败",
                "success": False,
            }


        return {
                "remark": "注册成功",
                "success": True,
        }


class UserLogin(Resource):

    def post(self):
        args = parser.parse_args()
        user_name = args.get('user_name')
        password = args.get('password')

        if not user_name:
            return {
                       "remark": "用户名为空",
                       "success": False,
                   }, 400
        if not password:
            return {
                       "remark": "密码为空",
                       "success": False,
                   }, 400

        user = SystemUser.query.filter(SystemUser.user_name.__eq__(user_name)).first()

        if user and user.check_password(password):
            token = generate_token()
            session[token] = user.user_id
            return {
                "remark": "登录成功",
                "success": True,
                "data": {
                    "token": token,
                    "user_info": marshal(user, user_fields)
                }
            }

        return {
            "remark": "用户名或密码错误",
            "success": False,
        }
