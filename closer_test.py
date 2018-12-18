


def fun():
    x = 9
    def inside():
        x = x + 1
        print()
    return inside


r = range(1, 10)
print(type(r))
for i in r:
    print(i)