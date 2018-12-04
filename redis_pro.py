import redis

if __name__ == '__main__':
    # decode_responses表名使用str而不是bytes类型
    r = redis.StrictRedis(host='10.10.32.167', port=16379, db=0, decode_responses=True)  # 显示指定主机、端口号和数据库
    members = r.smembers("robotchat:block:list:")
    get_str = r.get('relation.push.config')

    # print(get_str)
    for i in members:
        split = str(i).strip("\"").split("_")
        print('UPDATE `customer_relation` SET is_blocked=1 WHERE user_id=' + split[0] + ' and robot_id=' + split[1]+';')

    # s = b'hello\n'
    # s2 = 'hello\n'
    # s3 = str(s)
    # print(s, len(s), type(s))
    # print(s2, len(s2), type(s2))
    # print(s3, len(s3), type(s3))
