# -*- coding: utf-8 -*-
"""
excel读取的示例文件,
"""
import json

import pymysql
import xlrd


# 获取合并单元格的最下面部分
def get_merged_high_row(sheet, row_index, col_index):
    merged = sheet.merged_cells
    for (rlow, rhigh, clow, chigh) in merged:
        if row_index == rlow and col_index == clow:
            return rhigh
    return row_index


if __name__ == '__main__':
    connect_info = json.load(open('./spider/mysql_pass.i.json', 'r'))
    # 连接数据库
    conn = pymysql.connect(host=connect_info['host'], port=connect_info['port'], user=connect_info['user'],
                           passwd=connect_info['passwd'], autocommit=True)
    # formatting_info=True 用于保留合并单元格信息，默认不带
    ad_wb = xlrd.open_workbook("tags.xls", formatting_info=True)
    sheet = ad_wb.sheet_by_index(0)
    cursor = conn.cursor()
    cursor.execute("use `cpsp-song`")
    # 一级
    for i in range(1, sheet.nrows):
        if sheet.cell(i, 0).value != '':
            highRow = get_merged_high_row(sheet, i, 0)
            cursor.execute(
                "INSERT INTO `tbl_new_tag_info`(`parent_id`,`tag_name`) VALUES(0,%s);", (sheet.cell(i, 0).value))
            pid1 = cursor.lastrowid
            # 二级
            for j in range(i, highRow):
                if sheet.cell(j, 1).value != '':
                    highRow2 = get_merged_high_row(sheet, j, 1)
                    cursor.execute(
                        "INSERT INTO `tbl_new_tag_info`(`parent_id`,`tag_name`) VALUES(%s,%s);",
                        (pid1, sheet.cell(j, 1).value))
                    pid2 = cursor.lastrowid
                    # 三级
                    for k in range(j, highRow2):
                        if sheet.cell(k, 2).value != '':
                            highRow3 = get_merged_high_row(sheet, k, 1)
                            cursor.execute(
                                "INSERT INTO `tbl_new_tag_info`(`parent_id`,`tag_name`) VALUES(%s,%s);",
                                (pid2, sheet.cell(k, 2).value))
