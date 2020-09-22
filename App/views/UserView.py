from flask import Blueprint, render_template
from App.model import models, User

user_blue = Blueprint('user_blue', __name__)


# @user_blue.route('/')
# def index():
#     return render_template('login.html', msg="傻子啊")


@user_blue.route('/createdb/')
def createdb():
    models.create_all()
    return '创建成功'


@user_blue.route('/dropdb/')
def dropdb():
    models.drop_all()
    return '删除成功'


@user_blue.route('/adduser/')
def add_user():
    user = User()
    user.username = 'Tonne'
    user.save()
    return '创建成功'
