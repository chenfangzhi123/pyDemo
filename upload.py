import requests
import os
import json


def upload(file):
    _files = {"file": (file), "filename": "asdf.png"}
    _token = "16_67f48722b67b4fa2a4e75c06fa3a79c1"
    _header = {"X-Token": _token}
    result = requests.post("http://manager-api.mapple.fun/upload", files=_files, headers=_header)
    # result = requests.post("http://10.10.32.167:6012/upload", files=_files, headers=_header)
    try:
        res = json.loads(result.text)
        print(res['dataInfo'])
    except Exception as e:
        print(type(e), result)


if __name__ == "__main__":
    fileList = os.listdir("./head")
    for f in fileList:
        upload(open("./head/" + f, "rb"))
