import time

from App.ext import models


class SystemUser(models.Model):
    user_id = models.Column(models.Integer, primary_key=True)
    user_name = models.Column(models.String(50), nullable=False)
    user_avatar = models.Column(models.String(255), default='')
    password = models.Column(models.String(255), nullable=False)
    create_at = models.Column(models.Integer)
    update_at = models.Column(models.Integer, default=int(time.time()))
    authority = models.Column(models.String(255), default='{}')
    is_valid = models.Column(models.Boolean, default=True)

    def save(self):
        models.session.add(self)
        models.session.commit()
