import os
import shutil
from flask import request
from flask_restful import Resource

ori_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CopyImage(Resource):
    """恢复图片
    """

    def get(self):

        pic_name = request.form.get('name')
        pw = request.form.get('pw')

        keep_dir = os.path.join(ori_dir, 'static/img/keep/')
        imgs_li = os.listdir(keep_dir)

        images_dir = os.path.join(ori_dir, 'static/img/images/')
        imgs_li2 = os.listdir(images_dir)
        if pic_name in imgs_li and pic_name not in imgs_li2 and pw == 'admin':
            file_name = os.path.join(ori_dir, 'static/img/keep/%s' % pic_name)
            file_name2 = os.path.join(ori_dir, 'static/img/images/%s' % pic_name)
            shutil.copy(file_name, file_name2)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()


class DeleteKeep(Resource):
    """恢复图片
    """

    def get(self):

        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        keep_dir = os.path.join(ori_dir, 'static/img/keep/')
        imgs_li = os.listdir(keep_dir)

        if pic_name in imgs_li and pw == 'admin':
            file_name = os.path.join(ori_dir,'static/img/keep/%s' % pic_name)
            os.remove(file_name)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()
