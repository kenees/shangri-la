from flask import request


def load_middleware(app):

    @app.before_request
    def before():
        # print('中间件', request)
        pass
        """
            统计
            优先级
            反扒
            用户认证
            用户权限
        """
        

    @app.after_request
    def after(response):
        print('response', response)
        return response