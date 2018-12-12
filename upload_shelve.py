import requests
import shelve
import os
import json

base_path = r'C:\Users\chen\Desktop\001-200\001-200'


def upload(file):
    _files = {"file": (file), "filename": "asdf.png"}
    _token = "13_111430c1bf2c44cfa8febb781709795f"
    _header = {"X-Token": _token}
    # result = requests.post("http://manager-api.mapple.fun/upload", files=_files, headers=_header)
    result = requests.post("http://10.10.32.167:6012/upload", files=_files, headers=_header)
    try:
        res = json.loads(result.text)
        return res['dataInfo']
    except Exception as e:
        print(type(e), result)
        return ''


with shelve.open('upload_db') as db:
    try:
        count = db['counter']
    except KeyError:
        print("计数器为空")
        count = 0
    print("初始计数为：",count)
    # fileList = os.listdir(base_path)
    # for f in fileList:
    #     pic_list = []
    #     count += 1
    #     intern_dir = os.path.join(base_path, f)
    #     if os.path.isdir(intern_dir):
    #         for file in os.listdir(intern_dir):
    #             pic_list.append(upload(open(os.path.join(intern_dir, file), "rb")))
    #     else:
    #         print("该文件%s不是文件夹" % f)
    #     if len(pic_list) == 0:
    #         print("该文件夹：%s为空" % f)
    #     db['counter'] = count
    #     db['list_%s' % count] = pic_list
    #     db['head_%s' % count] = pic_list[0]
    for key, value in db.items():
        print(key, '    ', value)
