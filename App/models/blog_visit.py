from App.ext import models


class BlogVisit(models.Model):
    uid = models.Column(models.Integer, primary_key=True)
    user_name = models.Column(models.Integer)
    system = models.Column(models.String(64))
    browser = models.Column(models.String(64))
    ip = models.Column(models.Integer)
    visitors_number = models.Column(models.Integer, default=0)
    last_time = models.Column(models.DateTime)
    access_rights = models.Column(models.Boolean, default=True)

    def save(self):
        models.session.add(self)
        models.session.commit()
