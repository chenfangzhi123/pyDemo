def fun1(**kwargs):
    print("hello:%(name)s ! " % kwargs)


class IterTest:
    def __init__(self):
        self.value = 0

    def __next__(self):
        if self.value > 10:
            raise StopIteration
        else:
            self.value += 1
            return self.value

    def __iter__(self):
        return self


def simple_generator():
    yield 1


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new
            print("adsf:", new)
        else:
            print("NONE")


if __name__ == "__main__":
    g = repeater(10)
    print(next(g))
    print(g.send("hello,word!"))
    print(g.send("hello,word!2"))
# for i in IterTest():
#     print(i)

# for i in simple_generator():
#     print(i)
