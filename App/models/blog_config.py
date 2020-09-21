from App.ext import models


class BlogConfig(models.Model):

    # __tablename__ = 'config'   # 重新定义表名
    system_id = models.Column(models.Integer, primary_key=True)
    visitors_number = models.Column(models.Integer)
    authority = models.Column(models.String(255))

    def save(self):
        models.session.add(self)
        models.session.commit()
