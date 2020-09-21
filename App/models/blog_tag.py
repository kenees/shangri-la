from App.ext import models


class BlogTag(models.Model):
    tag_id = models.Column(models.Integer, primary_key=True)
    tag_name = models.Column(models.String(255))
    is_valid = models.Column(models.Boolean, default=True)
    create_at = models.Column(models.DateTime)
    update_at = models.Column(models.DateTime)

    def save(self):
        models.session.add(self)
        models.session.commit()
