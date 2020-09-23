import time

from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import models


class SystemUser(models.Model):
    user_id = models.Column(models.Integer, primary_key=True)
    user_name = models.Column(models.String(50), nullable=False)
    user_avatar = models.Column(models.String(255), default='')
    _password = models.Column(models.String(255), nullable=False)
    create_at = models.Column(models.Integer)
    update_at = models.Column(models.Integer, default=int(time.time()))
    authority = models.Column(models.String(255), default='{}')
    is_valid = models.Column(models.Boolean, default=True)

    # 将方法变成属性， 并禁止获取
    @property
    def password(self):
        raise Exception("Error Action: Password can't access")

    # 自动加密
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    # 封装校验密码的方法
    def check_password(self, password):
        return check_password_hash(self._password, password)

    def save(self):
        models.session.add(self)
        models.session.commit()
