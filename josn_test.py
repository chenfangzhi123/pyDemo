import json

if __name__ == '__main__':
    dic = {"hello": "word"}
    dump = json.dumps(dic)
    print(dump)
    load = json.loads(' {"hello": "word"}')
    print(type(load))
    print(load)
