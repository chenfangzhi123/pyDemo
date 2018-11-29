import requests
import os
import json


def upload(file):
    _files = {"file": file}
    _token = "13_07a62a89e4b34df185776f8d3d108694"
    _header = {"X-Token": _token}
    result = requests.post("http://10.10.32.167:6012/upload", files=_files, headers=_header)
    print(json.loads(result.text)['dataInfo'])


if __name__ == "__main__":
    fileList = os.listdir(".")
    for f in fileList:
        upload(f)
    print("OK")
