import os
import random
import re
import threading
import time

import requests


def handler(start, end, url, filename):
    header = {'Range': 'bytes=%d-%d' % (start, end)}
    with requests.get(url, headers=header, stream=True) as r:
        with open(filename, "r+b") as fp:
            fp.seek(start)
            var = fp.tell()
            fp.write(r.content)
        print('%s 下载完成' % filename)


def download(url, tittle, num_thread=10):
    print("开始下载：", tittle)
    r = requests.head(url)
    try:
        file_name = tittle
        file_size = int(r.headers['content-length'])
    except Exception as e:
        print("检查URL，或不支持多线程下载", e)
        return
    fp = open(file_name, "wb")
    fp.truncate(file_size)
    fp.close()
    part = file_size // num_thread
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:
            end = file_size
        else:
            end = start + part
        t = threading.Thread(target=handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': file_name})
        t.setDaemon(True)
        t.start()
    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


def random_ip():
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    d = random.randint(1, 255)
    return str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)


def get_cookie():
    with open('collector.cookie', 'r') as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)  # 1代表只分割一次
            cookies[name] = value
        return cookies


flag = 1
while flag <= 100:
    tittle = []
    base_url = 'http://91porn.com/view_video.php?viewkey='
    page_url = 'http://91porn.com/v.php?next=watch&page=' + str(flag)
    get_page = requests.get(url=page_url)
    view_key = re.findall(
        r'<a target=blank href="http://91porn.com/view_video.php\?viewkey=(.*)&page=.*&viewtype=basic&category=.*?">\n                    <img ',
        str(get_page.content, 'utf-8', errors='ignore'))
    print('第', flag, '页的大小为：', len(view_key))
    for key in view_key:
        try:
            headers = {'Accept-Language': 'zh-CN,zh;q=0.9',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
                       'X-Forwarded-For': random_ip(), 'referer': page_url,
                       'Content-Type': 'multipart/form-data; session_language=cn_CN'}
            s = requests.Session()
            base_req = s.get(url=base_url + key, headers=headers, verify=False)  # cookies=get_cookie(),
            html_content = str(base_req.content, 'utf-8', errors='ignore')
            video_url = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>', html_content)
            tittle = re.findall(r'<div id="viewvideo-title">(.*?)</div>', html_content, re.S)
            t = os.path.join('91下载', tittle[0].strip())
            if not os.path.exists(str(t)):
                try:
                    print(str(t) + '.mp4', str(video_url[0]))
                    download(str(video_url[0]), str(t) + '.mp4')
                except Exception as e:
                    print('下载文件出错！', t, e)
            else:
                print('已存在文件,跳过', t)
                time.sleep(2)
        except IndexError:
            print("索引错误")
        except Exception as e:
            print('未知错误！', e)
    flag = flag + 1
print('此页已下载完成，下一页是' + str(flag))
