#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from PIL import Image


# 居中裁剪图片
def middle_tailoring(img, res_path):
    width, height = img.size
    half_the_width = width / 2
    half_the_height = height / 2
    img4 = img.crop(
        (
            half_the_width - min(height, width) / 2,
            half_the_height - min(height, width) / 2,
            half_the_width + min(height, width) / 2,
            half_the_height + min(height, width) / 2
        )
    )
    img4.save(res_path)


# 向上裁剪
def up_tailoring(img, res_path):
    width, height = img.size
    img4 = img.crop((0, 0, width, width))
    img4.save(res_path)


if __name__ == "__main__":
    file = open("all.txt", "r")
    base_dir = "/fastdfs/storage/data/"
    for p_file in file:
        p_file = p_file.strip()
        complete_path = os.path.join(base_dir, p_file)
        if os.path.exists(complete_path):
            image_open = Image.open(complete_path)
            if image_open.size[0] > image_open.size[1]:
                # png和jpg格式不一样，会报错
                image_open = image_open.convert('RGB')
                middle_tailoring(image_open, complete_path)
                print("success：", complete_path)
            elif image_open.size[0] < image_open.size[1]:
                image_open = image_open.convert('RGB')
                up_tailoring(image_open, complete_path)
                print("success：", complete_path)
            else:
                print("ignore:", complete_path)
        else:
            print("no exixt：", complete_path)
