import json

from flask import Blueprint

from App.models import BlogTag

tags_blue = Blueprint('tags_blue', __name__)


@tags_blue.route('/tag_list')
def get_tag_list():
    tags = BlogTag.query.all()
    print('get tags list..')
    print(json.dumps(tags))
    return json.dumps(tags)


