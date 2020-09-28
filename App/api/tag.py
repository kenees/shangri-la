import time

from flask import request
from flask_restful import Resource, fields, marshal_with, marshal

from App.models import BlogTag

tags_fields = {
    "tag_id": fields.Integer,
    "tag_name": fields.String,
    "default_color": fields.String,
    "is_valid": fields.Boolean(default=True),
    "create_at": fields.Integer,
    "update_at": fields.Integer,
}


class Tags(Resource):

    def get(self):
        tag_list = BlogTag.query.all()
        length = len(tag_list)
        print('tag_list', tag_list)
        print(length)
        return {
            "remark": "get success",
            "success": True,
            "data": {
                "length": length,
                "tag_list": marshal(tag_list, tags_fields),
            },
        }

    def put(self):

        date = request.json
        if date is None or date.get("tag_id") is None:
            return {
                "remark": "tag_id不能为空",
                "success": False,
            }

        tag = BlogTag.query.get_or_404(date.get("tag_id"))
        print('tag', tag)
        if not tag:
            return {
                "remark": "标签不存在",
                "success": False,
            }

        tag_name = date.get('tag_name')
        default_color = date.get("default_color")
        is_valid = date.get("is_valid")
        print(tag_name, default_color, is_valid)
        if tag_name is not None:
            tag.tag_name = tag_name
        if default_color is not None:
            tag.default_color = default_color
        if isinstance(is_valid, bool):
            tag.is_valid = is_valid

        if not tag.save():
            return {
                "remark": "更新失败",
                "success": False,
            }

        return {
            "remark": "更新成功",
            "success": True,
            "data": marshal(tag, tags_fields)
        }

    def post(self):

        data = request.json
        if request and data:
            if data.get('tag_name') is None:
                return {
                    "remark": "标签名不能为空",
                    "success": False,
                }

        tag_name = data.get('tag_name')
        default_color = data.get("default_color")

        blog_tag = BlogTag()
        blog_tag.tag_name = tag_name
        blog_tag.create_at = int(time.time())

        if default_color is not None:
            blog_tag.default_color = default_color

        if not blog_tag.save():
            return {
                "remark": "创建失败",
                "success": False,
            }

        return {
            "remark": "创建成功",
            "success": True,
        }

    def delete(self, id):

        tag = BlogTag.query.get_or_404(id)

        if not tag:
            return {
                "remark": "tag is not found",
                "success": False,
            }
        if not tag.delete():
            return {
                "remark": "delete error",
                "success": False,
            }

        return {
            "remark": "delete success",
            "success": True,
        }
