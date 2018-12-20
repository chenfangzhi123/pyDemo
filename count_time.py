import datetime


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func(*args, **kwargs)
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = (over_time - start_time).total_seconds()
        print('方法%s,运行%s秒' % (func.__name__, total_time))
    return int_time


@count_time
def test(num):
    print("参数：", num)


if __name__ == '__main__':
    test(10)
