from flask import Blueprint

goods_blue = Blueprint('goods_blue', __name__)

@goods_blue.route('/goods')
def getGoodList():
    return 'good list'