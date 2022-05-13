from flask_restful import Resource
from flask import send_file, request, Response
import os
ori_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Robots(Resource):
    """爬虫爬取权限
    """

    def get(self):
        file_path = os.path.join(ori_dir,'static/favicon/robots.txt')
        return send_file(file_path)

    def post(self):
        return self.get()


class Favicon(Resource):
    """主页图标
    """

    def get(self):
        ico_path =  os.path.join(ori_dir,'static/favicon/favicon.ico')
        return send_file(ico_path)

    def post(self):
        return self.get()


class Picture(Resource):
    """主页图标
    """

    def get(self):
        pic_name = request.args.get('name')
        pic_name = pic_name[:23]
        file = request.args.get('file')
        file_name = os.path.join(ori_dir,'static/img/%s/%s' % (file, pic_name))
        with open(file_name, 'rb') as f:
            content = f.read()
        return Response(content, mimetype="image/jpeg")

    def post(self):
        return self.get()
