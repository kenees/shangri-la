from App.ext import models


class Article(models.Model):
    article_id = models.Column(models.Integer, primary_key=True)
    article_name = models.Column(models.String(255))
    article_tag = models.Column(models.String(255))
    create_at = models.Column(models.DateTime)
    update_at = models.Column(models.DateTime)
    reading_number = models.Column(models.Integer, default=0)
    edit_user = models.Column(models.String(50))
    comment_number = models.Column(models.Integer, default=0)

    def save(self):
        models.session.add(self)
        models.session.commit()
