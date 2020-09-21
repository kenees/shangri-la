from .user_blue import user_blue
from .goods_blue import goods_blue
from .tags_blue import tags_blue

base_url = '/api/v1/'


def init_view(app):
    app.register_blueprint(goods_blue, url_prefix=base_url)
    app.register_blueprint(user_blue, url_prefix=base_url)
    app.register_blueprint(tags_blue, url_prefix=base_url)