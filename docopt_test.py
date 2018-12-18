"""命令行火车票查看器
Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""

from docopt import docopt

# docopt是一个用于快速创建命令号程序界面的一个工具模块，重要的usage里面的字段，具体可以参见该模块的文档
arguments = docopt(__doc__, version='v1.0.0')
# print all
print(arguments)
print()

# 输出参数
print('出发>', arguments['<from>'])
print('达到>', arguments['<to>'])
print('时间>', arguments['<date>'])

# 处理选项 转换成list的格式
options = []
for key in arguments:
    if arguments[key] is True:
        # print (key)
        options.append(key)

# 输出选项
print("参数 >")
for x in options:
    print(x)

# 处理选项
sd = 'd'
sdd = '-' + sd
if (arguments[sdd] is True):
    print('-d in process')
