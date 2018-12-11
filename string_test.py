
if __name__ == "__main__":
    raw_str1 = r"hel\n\\noo\'hello\\"
    print(type(raw_str1))
    print(raw_str1)
    str1 = "hel\n\\noo\"hello\\"
    print(type(str1))
    print(str1)
    raw_str2 = r'''hello word!
    hello
    '''
    print(raw_str2)
