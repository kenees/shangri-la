import time
from flask import request
from flask_restful import Resource
from App.models import SystemUser


class UserRegister(Resource):

    def post(self):
        print(request)
        user_name = request.json.get('user_name')
        password = request.json.get('password')
        system_user = SystemUser()
        system_user.user_name = user_name
        system_user.password = password
        system_user.create_at = int(time.time())
        system_user.save()

        return { "msg": "register success" }


class UserLogin(Resource):

    def post(self):
        if request and request.json:
            user_name = request.json.get('user_name')
            password = request.json.get('password')
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
        else:
            return {
                "remark": "参数异常",
                "success": False,
            }, 400

        user = SystemUser.query.filter(SystemUser.user_name.__eq__(user_name)).first()
        if user and user.check_password(password):
            return {
                    "remark": "登录成功",
                    "success": True,
            }

        return {
            "remark": "用户名或密码错误",
            "success": False,
        }
