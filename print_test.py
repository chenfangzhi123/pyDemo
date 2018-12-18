if __name__ == '__main__':
    with open("print.txt", "w+") as file:
        print("hello", "word", sep=',', file=file)
        print("hello", "word", sep=',', file=file)
