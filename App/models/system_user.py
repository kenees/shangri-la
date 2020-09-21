from App.ext import models


class SystemUser(models.Model):
    user_id = models.Column(models.Integer, primary_key=True)
    user_name = models.Column(models.String(50))
    user_avatar = models.Column(models.String(255))
    password = models.Column(models.String(20))
    create_at = models.Column(models.DateTime)
    update_at = models.Column(models.DateTime)
    authority = models.Column(models.String(255))
    is_valid = models.Column(models.Boolean, default=True)

    def save(self):
        models.session.add(self)
        models.session.commit()
