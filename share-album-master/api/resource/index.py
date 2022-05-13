import os
import shutil
from PIL import Image
from flask import request
from flask_restful import Resource

ori_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class DeletePicture(Resource):
    """删除图片，将图片存到回收站
    """

    def get(self):
        image_dir = os.path.join(ori_dir, 'static/img/images')
        imgs_li = os.listdir(image_dir)
        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        if pic_name in imgs_li and pw == 'admin':
            file_name = os.path.join(ori_dir, 'static/img/images/%s' % pic_name)
            file_name2 = os.path.join(ori_dir, 'static/img/recycle/%s' % pic_name)
            shutil.move(file_name, file_name2)
            return "200"
        else:
            return "401"

    def post(self):
        return self.get()


class Revolve(Resource):
    def get(self):
        """
        旋转图片，将图片存到images文件夹里
        :return: 200
        """
        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        image_dir = os.path.join(ori_dir, 'static/img/images')
        imgs_li = os.listdir(image_dir)
        print(pic_name, imgs_li, pw, pic_name)
        if pic_name in imgs_li and pw == 'admin':
            file_name = os.path.join(ori_dir,'static/img/images/%s' % pic_name)
            img = Image.open(file_name)  # 打开图片
            img3 = img.transpose(Image.ROTATE_90)  # 旋转 90 度角。
            img3.save(file_name)
            return "200"
        else:
            return "401"

    def post(self):
        return self.get()
