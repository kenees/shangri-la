import time

from flask import request
from flask_restful import Resource

from App.models import BlogTag


class Tags(Resource):
    def get(self):
        return { "msg": "get tag list"}


    def post(self):

        date = request.json
        if date is None or date.get('tag_name') is None:
            return {"msg": "标签名不能为空"}

        tag_name = request.json.get('tag_name')
        default_color = request.json.get("default_color")

        blog_tag = BlogTag()
        blog_tag.tag_name = tag_name
        blog_tag.create_at = int(time.time())
        
        if default_color is not None:
            blog_tag.default_color = default_color

        blog_tag.save()

        return { "msg": "create tag success"}