import time
from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from App.ext import models
from App.models import SystemUser

system_user_blue = Blueprint('system_user_blue', __name__)


@system_user_blue.route('/user/register', methods=['POST'])
def user_register():
    print(request)
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    hash_pwd = generate_password_hash(password)
    system_user = SystemUser()
    system_user.user_name = user_name
    system_user.password = hash_pwd
    system_user.create_at = int(time.time())
    system_user.save()
    return "register success"


@system_user_blue.route('/user/login', methods=['POST'])
def user_login():
    user_name = request.json.get('user_name')
    password = request.json.get('password')

    user = SystemUser.query.filter(SystemUser.user_name.__eq__(user_name)).first()
    print(user)
    print(user.password)
    if user and check_password_hash(user.password, password):
        return "login success"

    return "用户名或密码错误"
