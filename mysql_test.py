from retry import retry
import time
import count_time
import datetime
from pprint import pprint
import pymysql
import json
import my_logging

connect_info = json.load(open('mysql_pass.i.json', 'r'))
# 连接数据库
conn = pymysql.connect(host=connect_info['host'], port=connect_info['port'], user=connect_info['user'],
                       passwd=connect_info['passwd'])
cursor = conn.cursor()
# cursor_execute = cursor.execute("use alpha_robot_chat")
# print(cursor.execute("select * from customer"))
# fetchall = cursor.fetchall()
# pprint.pprint(fetchall)

customers = [3, 4]
dates = []

init_date = datetime.datetime.strptime('2018-12-16', '%Y-%m-%d')
while init_date + datetime.timedelta(days=1) < datetime.datetime.now():
    dates.append(init_date)
    init_date += datetime.timedelta(days=1)


# res = datetime.datetime.strptime('2018-12-16', '%Y-%m-%d')
# print(res.timestamp())
# pprint(dates)

@retry(tries=3, delay=1)
@count_time.count_time
def do_query(customer, cur_date):
    print("客服id：%s,日期：%s" % (customer, cur_date.strftime('%Y-%m-%d')))
    cursor.execute('use alpha_robot_chat')
    end_date = cur_date + datetime.timedelta(days=1)
    # end_date = datetime.datetime.combine(cur_date, datetime.time.max).strftime('%Y-%m-%d %H:%M:%S')
    num = cursor.execute(
        'SELECT robot_id,user_id,create_time  FROM `customer_relation` WHERE customer_id=%s and create_time>=%s AND create_time<%s',
        (customer, cur_date, end_date))
    all_relation = cursor.fetchall()
    i = 0
    if len(all_relation) > 0:
        cursor.execute('use alpha_message')
        for relation in all_relation:
            cursor.execute(
                'select count(*) from user_message_chat_history where from_user_id=%s and to_user_id=%s and send_time>%s and send_time<%s',
                (relation[0], relation[1], relation[2], relation[2] + datetime.timedelta(days=1)))
            if cursor.fetchone()[0] > 0:
                i += 1
    print("关系数：%s,回复数：%s" % (num, i))


for c in customers:
    for d in dates:
        do_query(c, d)
