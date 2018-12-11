import redis
import time
import pprint

if __name__ == '__main__':
    start = time.time()
    # # decode_responses表名使用str而不是bytes类型
    r = redis.StrictRedis(host='10.10.32.167', port=16379, db=0, decode_responses=True)  # 显示指定主机、端口号和数据库
    # 采用管道版本
    # with r.pipeline(transaction=False) as p:
    #     for line in open('unread.txt'):
    #         key = line.strip()
    #         p.hdel('robotchat:unread:count:', key)
    #         p.zrem("robotchat:allocated:", key)
    #         p.sadd("robotchat:block:list:", key)
    #     execute = p.execute()
    #     pprint.pprint(execute)
    # print("总操作时间：", time.time() - start)

    # 采用多命令版本
    my_list = list(map(lambda x: x.strip(), open('unread.txt')))
    print(r.hdel('robotchat:unread:count:', *my_list))
    print(r.zrem("robotchat:allocated:", *my_list))
    print(r.sadd("robotchat:block:list:", *my_list))

    # members = r.smembers("robotchat:block:list:")
    # get_str = r.get('relation.push.config')
    #
    # # print(get_str)
    # for i in members:
    #     split = str(i).strip("\"").split("_")
    #     print(
    #         'UPDATE `customer_relation` SET is_blocked=1 WHERE user_id=' + split[0] + ' and robot_id=' + split[1] + ';')

    # s = b'hello\n'
    # s2 = 'hello\n'
    # s3 = str(s)
    # print(s, len(s), type(s))
    # print(s2, len(s2), type(s2))
    # print(s3, len(s3), type(s3))
