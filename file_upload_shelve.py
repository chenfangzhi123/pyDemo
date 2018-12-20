import logging
import requests
import shelve
import os
import json
from retry import retry

base_path = r'C:\Users\chen\Desktop\201-350'


def upload(image_file):
    _files = {"file": image_file, "filename": "temp.png"}
    _token = "16_3f52b074e128414da5cb0d5a4f355cbe"
    _header = {"X-Token": _token}
    result = requests.post("http://manager-api.mapple.fun/upload", files=_files, headers=_header)
    # result = requests.post("http://10.10.32.167:6012/upload", files=_files, headers=_header, )
    try:
        res = json.loads(result.text)
        return res['dataInfo']
    except Exception as e:
        print(type(e), result)
        return ''


@retry(tries=3, delay=1)
def upload_file():
    pic_list.append(upload(open(os.path.join(intern_dir, file), "rb")))


with shelve.open('upload_db') as db:
    # logging.warning("开始执行！")
    # count = 4994
    # print("初始计数：", count)
    # fileList = os.listdir(base_path)
    # for f in fileList:
    #     count += 1
    #     print("当前上传计数：", count)
    #     pic_list = []
    #     intern_dir = os.path.join(base_path, f)
    #     if os.path.isdir(intern_dir):
    #         for file in os.listdir(intern_dir):
    #             try:
    #                 upload_file()
    #             except ConnectionError as e:
    #                 print("上传错误，exception：", e)
    #     else:
    #         print("该文件%s不是文件夹" % f)
    #     if len(pic_list) == 0:
    #         print("该文件夹：%s为空" % f)
    #     else:
    #         db['list_%s' % count] = pic_list
    #         db['head_%s' % count] = pic_list[0]

    # 头像
    for key, value in db.items():
        if key.startswith("head"):
            print(int(key.split("_")[1]), ',"'+ value+'"')
    # # 图片
    # for key, value in db.items():
    #     if key.startswith("list"):
    #         id = int(key.split("_")[1])
    #         for i, t in enumerate(value):
    #             head = 0
    #             if i == 0:
    #                 head = 1
    #             print(id, ',"' + value[i] + '"', ',"' + value[i] + '",', head)
