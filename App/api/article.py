import time

from flask import request
from flask_restful import Resource, fields, reqparse, marshal
from App.models import Article

article_fields = {
    "article_id": fields.Integer,
    "article_name": fields.String,
    "article_content": fields.String,
    "article_tag": fields.String,
    "is_valid": fields.Boolean(default=True),
    "create_at": fields.Integer,
    "update_at": fields.Integer,
    "reading_number": fields.Integer,
    "edit_user": fields.String,
    "comment_number": fields.Integer,
}

# 输入过滤
parser = reqparse.RequestParser()
parser.add_argument("article_id", required=False)
parser.add_argument("article_name")
parser.add_argument("article_tag")
parser.add_argument("article_content")
parser.add_argument("start_time")
parser.add_argument("end_time")
parser.add_argument("edit_user")
parser.add_argument("is_valid", type=bool)

parser_put = parser.copy()
parser_put.add_argument("article_id", required=True)


class ArticleResource(Resource):

    def get(self):
        args = parser.parse_args()
        article_id = args.get("article_id")
        article_name = args.get("article_name")
        start_time = args.get("start_time") or 0
        end_time = args.get("end_time") or time.time()

        print('start_time', start_time)
        print('end_time', end_time)

        if not article_id and not article_name:
            article_list = Article.query \
                .filter(Article.update_at > start_time) \
                .filter(Article.update_at < end_time) \
                .all()
        elif article_id:
            article_list = Article.query \
                .filter(Article.article_id == article_id) \
                .filter(Article.article_name.contains(article_name)) \
                .filter(Article.update_at > start_time) \
                .filter(Article.update_at < end_time) \
                .all()
        else:
            article_list = Article.query\
                .filter(Article.article_name.contains(article_name)) \
                .filter(Article.update_at > start_time) \
                .filter(Article.update_at < end_time) \
                .all()

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
        args = parser_put.parse_args()
        article = Article.query.get_or_404(args.get("article_id"))
        print('article', article)
        if not article:
            return {
                "remark": "文章不存在",
                "success": False,
            }

        article_name = args.get('article_name')
        article_content = args.get('article_content')
        article_tag = args.get("article_tag")
        edit_user = args.get("edit_user")
        is_valid = args.get("is_valid")
        print(article_name, article_tag, edit_user, is_valid, article_content)
        if article_name is not None:
            article.article_name = article_name
        if article_content is not None:
            article.article_content = article_content
        if article_tag is not None:
            article.article_tag = article_tag
        if edit_user is not None:
            article.edit_user = edit_user
        if is_valid is not None:
            article.is_valid = is_valid
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
        args = parser.parse_args()
        article_name = args.get('article_name')
        is_valid = args.get("is_valid")
        article_content = args.get("article_content")
        edit_user = args.get("edit_user")
        article_tag = args.get("article_tag")

        article = Article()
        article.article_name = article_name
        article.article_content = article_content
        article.edit_user = edit_user
        article.is_valid = is_valid
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

    def delete(self):
        args = parser_put.parse_args()
        article = Article.query.get_or_404(args.get("article_id"))

        if not article:
            return {
                "remark": "article is not found",
                "success": False,
            }
        if not article.delete():
            return {
                "remark": "delete fail",
                "success": False,
            }

        return {
            "remark": "delete success",
            "success": True,
        }
