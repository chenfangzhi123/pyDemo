import pprint

rectangle = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rectangle2 = [[1, 2], [3, 4]]
rectangle3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rectangle4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

'''
翻转90度矩形,1.6题
'''


def convert(rect):
    n = len(rect)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # print(i, j)
            temp = rect[i][j]
            rect[i][j] = rect[n - j - 1][i]
            rect[n - j - 1][i] = rect[n - i - 1][n - j - 1]
            rect[n - i - 1][n - j - 1] = rect[j][n - i - 1]
            rect[j][n - i - 1] = temp


if __name__ == '__main__':
    # for i in range(4):
    #     print(i)

    convert(rectangle)
    convert(rectangle2)
    convert(rectangle3)
    convert(rectangle4)
    pprint.pprint(rectangle)
    pprint.pprint(rectangle2)
    pprint.pprint(rectangle3)
    pprint.pprint(rectangle4)
