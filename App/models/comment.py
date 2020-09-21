from App.ext import models


class Comment(models.Model):
    comment_id = models.Column(models.Integer, primary_key=True)
    topic_id = models.Column(models.Integer)
    content = models.Column(models.String(255))
    from_uid = models.Column(models.Integer)
    comment_date = models.Column(models.DateTime)

    def save(self):
        models.session.add(self)
        models.session.commit()
