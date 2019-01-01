# py中所有的参数传递可以理解为java中的传递，传递的是一个参数的引用(对应c中的指针)
def test_immutable_for_simpledata(args):
    print('============')
    print(2, id(args))
    args = args + 10
    print(3, args)
    print(4, id(args))
    print('============')


if __name__ == '__main__':
    cur = 5000
    print(1, id(cur))
    test_immutable_for_simpledata(cur)
    print(5, cur)
    print(6, id(cur))


