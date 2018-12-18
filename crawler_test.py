# from urllib import request
import urllib

url = "http://www.baidu.com"

urlopen = urllib.request.urlopen(url, timeout=10)
print(urlopen.read().decode("utf-8"))
