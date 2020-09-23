import time
from flask import Blueprint, request
from flask_mail import Message

from App.ext import mail
from App.models import SystemUser

system_user_blue = Blueprint('system_user_blue', __name__)


@system_user_blue.route('/user/register', methods=['POST'])
def user_register():
    print(request)
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    system_user = SystemUser()
    system_user.user_name = user_name
    system_user.password = password
    system_user.create_at = int(time.time())
    system_user.save()
    return "register success"


@system_user_blue.route('/user/login', methods=['POST'])
def user_login():
    user_name = request.json.get('user_name')
    password = request.json.get('password')

    user = SystemUser.query.filter(SystemUser.user_name.__eq__(user_name)).first()
    if user and user.check_password(password):
        return "login success"

    return "用户名或密码错误"


@system_user_blue.route('/user/sendmail')
def send_mail():
    msg = Message("flask email", recipients=["17621969165@163.com",])     # 接受者列表
    msg.body = "哈哈， 大佬"
    msg.html = "<h3>你是个天才</h3>"
    mail.send(message=msg)

    return '邮件发送成功'
