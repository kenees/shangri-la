from App.ext import models


class BlogTag(models.Model):
    tag_id = models.Column(models.Integer, primary_key=True)
    tag_name = models.Column(models.String(32), index=True, unique=True)
    default_color = models.Column(models.String(32), default="rgb(134, 137, 140)")
    is_valid = models.Column(models.Boolean, default=True)
    create_at = models.Column(models.Integer)
    update_at = models.Column(models.Integer, default=create_at)

    def save(self):
        try:
            models.session.add(self)
            models.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    #
    # def update_tag(tag, attr):
    #     tag.update(attr)
    #     models.session.commit()

    def delete(self):
        try:
            models.session.delete(self)
            models.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
