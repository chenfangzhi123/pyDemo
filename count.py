import sys

result = {}
if __name__ == '__main__':
    for ln in sys.stdin:
        try:
            split = ln.split()
            od = split[0]
            for idx, val in enumerate(split[3].split(";")):
                if val.split(":")[2] == "1":
                    key = od + "_" + val.split("|")[0]
                    if not result.has_key(key):
                        result[key] = set([])
                    result[key].add(split[1])
        except Exception as e:
            print "error:", e

    for key, val in result.iteritems():
        f = open("xunfei" + key, "a")
        for m in val:
            f.write(m + "\n")
        f.close()
