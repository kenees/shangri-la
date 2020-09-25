import time

from flask import request
from flask_restful import Resource, fields, marshal_with

from App.models import BlogTag

tags_fields = {
    "id": fields.Integer(attribute='tag_id'),
    "tag_name": fields.String,
    "default_color": fields.String,
    "is_valid": fields.Boolean(default=True),
    "create_at": fields.Integer,
    "update_at": fields.Integer,
}

single_list_fields = {
    "remark": fields.String,
    "success": fields.Boolean,
    "data": fields.Nested(tags_fields)
}


class Tags(Resource):

    @marshal_with(single_list_fields)
    def get(self):
        tag_list = BlogTag.query.all()
        print('tag_list', tag_list)
        return {
            "remark": "get success",
            "success": True,
            "data": tag_list,
        }

    def put(self):

        date = request.json
        if date is None or date.get("tag_id") is None:
            return {"msg": "参数错误"}

        tag = BlogTag.query.get_or_404(date.get("tag_id"))
        print('tag', tag)
        if tag is None:
            return {"msg": "tag不存在"}

        tag_name = date.get('tag_name')
        default_color = date.get("default_color")
        is_valid = date.get("is_valid")
        print(tag_name, default_color, is_valid)
        if tag_name is not None:
            tag.update(tag_name=tag_name)
        if default_color is not None:
            tag.update(default_color=default_color)
        if isinstance(is_valid, bool):
            tag.update(is_valid=is_valid)

        tag.save()
        return {"msg": "update tag success"}

    def post(self):

        date = request.json
        if date is None or date.get('tag_name') is None:
            return {"msg": "标签名不能为空"}

        tag_name = date.get('tag_name')
        default_color = date.get("default_color")

        blog_tag = BlogTag()
        blog_tag.tag_name = tag_name
        blog_tag.create_at = int(time.time())

        if default_color is not None:
            blog_tag.default_color = default_color

        blog_tag.save()

        return {"msg": "create tag success"}
