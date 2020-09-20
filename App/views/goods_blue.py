import json
import random
from flask import Blueprint, redirect, url_for, request, abort, render_template, Response, session
from App.model import User
from App.ext import models

goods_blue = Blueprint('goods_blue', __name__)

# 转换器
# <string: str> 默认 以/结尾
# <path: pp>
# 从path开始，后面的都是path
# <int: id> 数字
# <float: id>  浮点数
# <uuid: uuid>  uuid  特殊id
# <any(a,b):an>   只能匹配小括号中写有的值


@goods_blue.route('/goods/list/<int:id>/')
@goods_blue.route('/goods/<int:id>/', methods=['GET'])
def getGoodList(id):
    print('di', id)
    return 'good list id '


# 重定向
@goods_blue.route('/redirect/')
def red():
    # return redirect('/goods/123/')
    return redirect(url_for('goods_blue.getGoodList', id=111))

@goods_blue.route('/getrequest')
def get_request():
    # print(request.host)
    # print(request.url)
    # if request.method == 'GET':
    #     return "GET SUCCESS"
    # elif request.method == "POST":
    #     return "POST SUCCESS"
    # else:
    #     return '%s success' % request.method

    # 按照状态码直接报错
    abort(401)


# 会话技术
@goods_blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get("username")

        response = Response("登录成功%s" % username)
        # 将登录信息存在cookie中
        # response.set_cookie('username', username)
        # 将 session 存入redis中
        session['username'] = username
        session['password'] = username
        return response

@goods_blue.route('/mine/')
def mine():
    # username = request.cookies.get('username')
    username = session.get('username')
    return "欢迎回来%s" % username


# 添加一个数据
@goods_blue.route('/addstudent/')
def add_student():

    user = User()
    user.username = "小王%d" % random.randrange(10000)
    user.save()
    return 'add success'

# 添加一组数据
@goods_blue.route('/addstudents/')
def add_students():
    students = []
    for i in range(5):
        student = User()
        student.username = '小天%d' % i
        students.append(student)

    print(students)
    models.session.add_all(students)
    models.session.commit()

    return 'add all success'

# 根据id查询数据
@goods_blue.route('/get_student/')
def get_student():
    # student = User.query.first()
    # return student.username

    # student = User.query.get_or_404(2)
    # return student.username

    student = User.query.get(4)
    # return student.username
    return json.dumps(student)

# 查询所有
@goods_blue.route('/get_all_student/')
def get_all_students():

    students = User.query.all()
    print(students)
    return 'get all students success'


# 删除数据
@goods_blue.route('/delete_student/')
def delete_student():
    student = User.query.first()

    models.session.delete(student)
    models.session.commit()

    return 'delete success'


# 更新数据
@goods_blue.route('/update_student/')
def update_student():
    student = User.query.first()
    student.username = '沙箱'
    models.session.add(student)
    models.session.commit()

    return 'update success'

# 捕获错误状态进行异常处理
@goods_blue.errorhandler(401)
def handle_error(error):
    print(error)
    return 'what'