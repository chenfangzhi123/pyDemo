import json
import re

import pymysql
import requests

connect_info = json.load(open('mysql_pass.i.json', 'r'))
print(connect_info)
# 连接数据库
conn = pymysql.connect(host=connect_info['host'], port=connect_info['port'], user=connect_info['user'],
                       passwd=connect_info['passwd'], charset='utf8mb4', autocommit=True)
cursor = conn.cursor()
cursor.execute('use `cpsp-song`')

num = cursor.execute('SELECT singer  FROM `tbl_base_info_singer_bak2` WHERE done=0')
print("totol:{}".format(num))
singers = cursor.fetchall()
cache = {}
for singer in singers:
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
                           'Cookie'
    }
    base_url = "http://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?is_xml=0&key={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"
    # myurl = base_url.format('毛不易')

    try:
        search = singer[0]
        find1 = singer[0].find('、')
        find2 = singer[0].find('(')
        find3 = singer[0].find('，')
        find4 = singer[0].find('（')
        l = []
        if find1 > 0:
            l.append(find1)
        if find2 > 0:
            l.append(find2)
        if find3 > 0:
            l.append(find3)
        if find4 > 0:
            l.append(find4)
        if len(l) > 0:
            index = min(l)
            search = singer[0][:index]
        myurl = base_url.format(search)
        if search in cache:
            cursor.execute(
                'UPDATE tbl_base_info_singer_bak2 SET `done`=1 ,state=%s , birthday=%s ,birthplace=%s,search=%s where singer=%s',
                (cache[search][0], cache[search][1], cache[search][2], search, singer[0]))
            print("缓存命中，singer:{},search:{}".format(singer[0], search))
            conn.commit()
            continue

        # time.sleep(0.1)
        base_req = requests.get(url=myurl, headers=headers)  # cookies=get_cookie(),
        base_req.encoding = 'utf-8'
        req_json = base_req.json()
        if 'data' in req_json and 'singer' in req_json['data'] and 'itemlist' in req_json['data']['singer'] and len(
                req_json['data']['singer']['itemlist']) > 0:
            mid = req_json['data']['singer']['itemlist'][0]['mid']
            base_req = requests.get(url='https://y.qq.com/n/yqq/singer/{}.html'.format(mid), headers=headers)
            text = base_req.text
            state = re.findall(r'国籍：(.*?)\</p\>', text)
            birthday = re.findall(r'出生日期：(.*?)\</p\>', text)
            birthPlace = re.findall(r'出生地：(.*?)\</p\>', text)
            q1 = ''
            q2 = ''
            q3 = ''
            if len(state) > 0:
                q1 = state[0]
            if len(birthday) > 0:
                q2 = birthday[0]
            if len(birthPlace) > 0:
                q3 = birthPlace[0]
            print('歌手名：{}，查找名：{}，国籍：{}，出生日期：{}，出生地：{}'.format(singer[0], search, q1, q2, q3))
            cursor.execute(
                'UPDATE tbl_base_info_singer_bak2 SET `done`=1 ,state=%s , birthday=%s ,birthplace=%s,search=%s where singer=%s',
                (q1, q2, q3, search, singer[0]))
            cache[search] = (q1, q2, q3)
            conn.commit()
        else:
            print('歌手名：{},查找名：{},未找到'.format(singer[0], search))
            cursor.execute(
                'UPDATE tbl_base_info_singer_bak2 SET `done`=4 ,state=%s , birthday=%s ,birthplace=%s,search=%s where singer=%s',
                ('', '', '', search, singer[0]))
            cache[search] = ('', '', '')
            conn.commit()

    except Exception as e:
        print(type(e), e, "singer name:", singer)
