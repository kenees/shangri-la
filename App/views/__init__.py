from .user_blue import user_blue
from .goods_blue import goods_blue

def init_view(app):
    app.register_blueprint(goods_blue)
    app.register_blueprint(user_blue)