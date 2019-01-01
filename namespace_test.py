# 例子1
# def func():
#     variable = 100
#     print(variable)
#
#
# def test():
#     print(variable)
#
# test()
# print(variable)

# 例子2,
variable = 300


def test_scopt():
    print(variable)  # variable是test_scopt()的局部变量，但是在打印时并没有绑定内存对象。
    variable = 200


test_scopt()
print(variable)
