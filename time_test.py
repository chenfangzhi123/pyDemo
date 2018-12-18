import time
import  datetime

print(type(time.time()))
print(time.localtime())
print(time.strftime("%Y %m %d"))

print("---------")
now = datetime.datetime.now()
print(now)
time_delta=datetime.timedelta(minutes=10)
print(now + datetime.timedelta(minutes=10))

one_day = datetime.datetime(2008, 8, 20)
print(one_day + datetime.timedelta(days=10))


