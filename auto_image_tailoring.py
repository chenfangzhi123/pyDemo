import os
from PIL import Image

'本地图片处理代码'


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
    base_dir = r"C:\Users\chen\Desktop\201-350"
    listdir = os.listdir(base_dir)
    for parent_dir in listdir:
        if os.path.isfile(parent_dir):
            print("这个路径不是文件夹：", parent_dir)
        else:
            for f in os.listdir(os.path.join(base_dir, parent_dir)):
                complete_path = os.path.join(base_dir, parent_dir, f)
                try:
                    if not os.path.isfile(complete_path):
                        print("此文件不存在:", complete_path)
                    elif os.path.exists(complete_path):
                        image_open = Image.open(complete_path)
                        if image_open.size[0] > image_open.size[1]:
                            middle_tailoring(image_open, complete_path)
                        elif image_open.size[0] < image_open.size[1]:
                            up_tailoring(image_open, complete_path)
                    else:
                        print("文件不存在：")
                except Exception as e:
                    print("处理图片异常：", complete_path)
                    os.remove(complete_path)
