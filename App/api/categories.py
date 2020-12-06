from flask_restful import Resource, fields, reqparse, marshal

from App.models import Article

article_fields = {
    "article_id": fields.Integer,
    "article_title": fields.String,
    "article_describe": fields.String,
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
parser.add_argument("tag_id")


class CategoriesResource(Resource):
    def get(self):
        args = parser.parse_args()
        tag_id = args.get("tag_id")
        print('tag_id', tag_id)
        if not tag_id:
            articles = Article.query.all()
        else:
            articles = Article.query.filter(Article.article_tag.contains(tag_id)).all()

        length = len(articles)
        return {
            "remark": "get success",
            "success": True,
            "data": {
                "total": length,
                "article_list": marshal(articles, article_fields),
            }
        }

