from flask_restful import Api

from .article import ArticleResource
from .categories import CategoriesResource
from .system_user import UserRegister, UserLogin
from .tag import Tags

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(UserRegister, '/api/v1/user/register')
api.add_resource(UserLogin, '/api/v1/user/login')
api.add_resource(Tags, '/api/v1/tags')
api.add_resource(ArticleResource, '/api/v1/article')
api.add_resource(CategoriesResource, '/api/v1/categories')