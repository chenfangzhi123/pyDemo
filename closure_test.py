def outer():
    temp = 1

    def inner():
        nonlocal temp
        print(temp)  # 1
        temp += 1

    return inner


foo = outer()
foo()
foo()
foo()

print(foo.__closure__)  # 2 doctest: +ELLIPSIS
