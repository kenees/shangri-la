# 扩展库初始化
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    models.init_app(app)
    migrate.init_app(app, models)
    Session(app)