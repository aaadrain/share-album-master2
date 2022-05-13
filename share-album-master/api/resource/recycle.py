import os
import shutil
from flask import request
from flask_restful import Resource

ori_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Recover(Resource):
    """删除图片
    """
    def get(self):

        pic_name = request.form.get('name')
        pw = request.form.get('pw')

        imgs_li = os.listdir(os.path.join(ori_dir,'static/img/recycle'))
        if pic_name in imgs_li and pw == 'admin':

            file_name = os.path.join(ori_dir,'static/img/images/%s' % pic_name)
            file_name2 = os.path.join(ori_dir,'static/img/recycle/%s' % pic_name)
            shutil.move(file_name2, file_name)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()


class DeleteRecyclePicture(Resource):
    """删除回收站图片
    """

    def get(self):
        """
        删除图片的接口，将图片存到清空站
        :return: 200
        """

        imgs_li = os.listdir(os.path.join(ori_dir,'static/img/recycle'))
        pic_name = request.args.get('name')
        pw = request.form.get('pw')
        print(pic_name)
        if pic_name in imgs_li and pw == 'admin':
            file_name =  os.path.join(ori_dir,'static/img/recycle/%s' % pic_name)
            os.remove(file_name)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()


class DeleteAllRecyclePicture(Resource):
    """删除所有回收站里的图片
    """
    def get(self):
        pic_li = os.listdir(os.path.join(ori_dir,'static/img/recycle'))
        pw = request.form.get('pw')
        if pic_li and pw == 'admin':
            for name in pic_li:
                file_name = os.path.join(ori_dir,'static/img/recycle/%s' % name)
                os.remove(file_name)
            return '200'
        else:
            return '401'

    def post(self):
        return self.get()
