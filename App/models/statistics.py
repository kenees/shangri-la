from App.ext import models


class Statistics(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    pv_h = models.Column(models.Integer)
    pv_n = models.Column(models.Integer)
    uv_h = models.Column(models.Integer)
    uv_n = models.Column(models.Integer)
    ip_h = models.Column(models.Integer)
    ip_n = models.Column(models.Integer)
    vv_h = models.Column(models.Integer)
    vv_n = models.Column(models.Integer)

    def save(self):
        models.session.add(self)
        models.session.commit()
