from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from App.ext import init_ext
from App.settings import envs
from App.views import init_view


def create_app(env):
    app = Flask(__name__)

    # uri    数据库+驱动://用户名:密码@主机:端口
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db_user:eSD2mmrj6kHGRA8Y@122.51.240.250:3306/db_user'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 加载配置文件
    app.config.from_object(envs.get(env))

    init_ext(app)

    init_view(app)

    return app