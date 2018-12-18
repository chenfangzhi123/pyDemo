if __name__ == '__main__':
    code_str = "for i in range(0,10): print(i)"
    c = compile(code_str, '', 'exec')
    if 1 == 1:
        i = 9
    print(i)
    # exec(c)
