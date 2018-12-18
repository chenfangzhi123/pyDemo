import time
import timeit


def sleep_1_second():
    print("*" * 20)
    time.sleep(0.1)
    raise KeyError
    # return 10


if __name__ == '__main__':
    print("执行时间", timeit.timeit(sleep_1_second, number=3))
    print("执行时间", timeit.repeat(sleep_1_second, number=3, repeat=2))
