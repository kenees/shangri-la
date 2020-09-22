from .UserView import user_blue
from .GoodsView import goods_blue
from .TagsView import tags_blue
from .SystemUserView import system_user_blue

base_url = '/api/v1/'


def init_view(app):
    app.register_blueprint(goods_blue, url_prefix=base_url)
    app.register_blueprint(user_blue, url_prefix=base_url)
    app.register_blueprint(tags_blue, url_prefix=base_url)
    app.register_blueprint(system_user_blue, url_prefix=base_url)