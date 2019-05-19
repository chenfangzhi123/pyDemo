import re, fileinput

if __name__ == '__main__':
    print(re.escape("bt waf sadf?"))
    match = re.match("(bt) waf sadf(\\?)", "bt waf sadf?123")
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))

    print(match.groups())
    print(match.group())
    print(match)

    print("重复分组------------")
    print(re.findall(r"hello", "hellohello word"))
    print(re.findall(r"(hello)(\1)", "hellohello word"))
    """
        如果要实现上面打印hellohello而不输出额外的，
        下面的代码我没办法只取出hello9hello，将前面的组设置为?:之后后面就没办法捕获了,可以通过后面的match来取
    """
    findall = re.findall(r"(([a-z]{1,5}).?\2)", "hello9hello word9word")
    print("findall:", findall)
    print("match:", re.match(r"(([a-z]{1,5}).?\2)", "hello9hello word9word").group(1))

    print("正向肯定预查------------------")
    '正向肯定预查,预查不消耗字符，每次查询完后从上次匹配之后开始（不包括预查的字符，等于说匹配还会把上次预查的字符算进去）'
    """ 这里是匹配两次，输出是逗号分隔，：['win', 'win']' """
    print(re.findall("(win)(?=win)", "winwinwin"))
    """ 注意这里是匹配一次，输出的是元组：[('win', 'win')] """
    print(re.findall("(win)(win)", "winwinwin"))

    print("贪婪匹配---------")
    str="FROM: chenfa<>n><><><<.><<g<>zhi <1242692800@qq.com>"
    match_res = re.match("FROM: (.*) <.*>$", str)
    if match_res:
        print(match_res.group(1))
