import time

from flask import request
from flask_restful import Resource, fields, marshal_with, marshal

from App.models import Article

article_fields = {
    "id": fields.Integer(attribute='article_id'),
    "article_name": fields.String,
    "article_tag": fields.String,
    "create_at": fields.Integer,
    "update_at": fields.Integer,
    "reading_number": fields.Integer,
    "edit_user": fields.String,
    "comment_number": fields.Integer,
}


class ArticleResource(Resource):

    def get(self):
        article_list = Article.query.all()
        length = len(article_list)
        print('article_list', article_list)
        return {
            "remark": "get success",
            "success": True,
            "data": {
                "total": length,
                "article_list": marshal(article_list, article_fields),
            }
        }

    def put(self):

        date = request.json
        if date is None or date.get("article_id") is None:
            return {
                "remark": "参数错误",
                "success": False,
            }

        article = Article.query.get_or_404(date.get("article_id"))
        print('article', article)
        if not article:
            return {
                "remark": "文章不存在",
                "success": False,
            }

        article_name = date.get('article_name')
        article_tag = date.get("article_tag")
        edit_user = date.get("edit_user")
        print(article_name, article_tag, edit_user)
        if article_name is not None:
            article.article_name = article_name
        if article_tag is not None:
            article.article_tag = article_tag
        if edit_user is not None:
            article.edit_user = edit_user
        article.update_at = int(time.time())

        if not article.save():
            return {
                "remark": "更新失败",
                "success": False,
            }

        return {
            "remark": "更新成功",
            "success": True,
            "data": marshal(article, article_fields)
        }

    def post(self):

        date = request.json
        if date is None:
            return {"msg": "参数不能为空"}
        elif date.get('article_name') is None:
            return {"msg": "article_name不能为空"}
        elif date.get('article_content') is None:
            return {"msg": "article_content不能为空"}
        elif date.get('edit_user') is None:
            return {"msg": "edit_user不能为空"}

        article_name = date.get('article_name')
        article_content = date.get("article_content")
        edit_user = date.get("edit_user")
        article_tag = date.get("article_tag")

        article = Article()
        article.article_name = article_name
        article.article_content = article_content
        article.edit_user = edit_user
        if article_tag is not None:
            article.article_tag = article_tag
        article.create_at = int(time.time())

        if not article.save():
            return {
                "remark": "创建失败",
                "success": False,
            }

        return {
            "remark": "创建成功",
            "success": True,
            "data": marshal(article, article_fields)
        }

    def delete(self, id):

        article = Article.query.get_or_404(id)

        if not article:
            return {
                "remark": "tag is not found",
                "success": False,
            }
        if not article.delete():
            return {
                "remark": "delete error",
                "success": False,
            }

        return {
            "remark": "delete success",
            "success": True,
        }
