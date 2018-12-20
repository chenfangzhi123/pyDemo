import time
import my_logging
from retry import retry


@retry(tries=3, delay=1)
def test_fun():
    print("执行一次！")
    time.sleep(1)
    raise RuntimeError


if __name__ == '__main__':
    my_logging.logger.warning("start process!")
    test_fun()
