import sys
from urllib import parse

import requests

headers = {
    'authority': 'www.aliexpress.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

base_url = "https://www.aliexpress.com/glosearch/api/product?trafficChannel=main&d=y&CatId=0&SearchText={}&ltype=wholesale&SortType=default&page={}&origin=y"
# print(type(base_url))

referer = "https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={}&ltype=wholesale&SortType=default&page={}"
# print(type(referer))

# 读书
if len(sys.argv) < 3:
    print("至少输入关键字和店铺名")
    exit(1)

# 关键字
keyword = sys.argv[1]
# 店铺名称
store_name = sys.argv[2]
# 从第一页开始查找，最多查找的页面
pageTotal = 15
print("搜索关键字：%s, 店铺名：%s" % (keyword, store_name))

if len(sys.argv) >= 4:
    print("搜索页数：%s" % sys.argv[3])
    pageTotal = sys.argv[3]
plus = parse.quote_plus(keyword)

# 读取cookie文件设置header
with open("cookie.txt", "r") as t:
    lines = t.readlines()  # 读取所有行
    headers["cookie"] = lines[0].strip()

for i in range(pageTotal):
    print("当前查找页面：{}".format(i))
    j = 1 if i == 0 else i
    headers["referer"] = referer.format(plus, i)
    base_req = requests.get(url=base_url.format(plus, i + 1), headers=headers)  # cookies=get_cookie(),
    base_req.encoding = 'utf-8'
    req_json = base_req.json()
    if "items" in req_json:
        items_ = req_json["items"]
        # print(items_)
        for item in items_:
            if "store" in item and "storeName" in item["store"]:
                if store_name == item["store"]["storeName"]:
                    print("查找店铺：{}，在{}页，商品信息：{}".format(item["store"]["storeName"], i + 1, item))
                    exit(0)
                elif store_name in item["store"]["storeName"]:
                    print("有一个商品店铺名字包含了输入的店铺名关键字，店铺名：{}，在{}页，商品信息：{}".format(item["store"]["storeName"], i + 1, item))
            else:
                print("未包含店铺信息")

    else:
        print("没有返回商品信息")
        print(req_json)
