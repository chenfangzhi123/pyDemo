# -*- coding: utf-8 -*-
"""
excel操作的示例文件
"""
import xlwt
import datetime
import sys


# 字体设置
def style(bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = bold
    font.color_index = 4
    style.font = font
    return style


def write_excel(file, dsp_name, title, values):  # 写入xls部分

    print dsp_name
    # 第二参数用于确认同一个cell单元是否可以重设值。
    sheet1 = file.add_sheet(dsp_name)

    for i in range(len(title)):
        sheet1.col(i).width = 350 * len(title[i])
        sheet1.write(0, i, title[i], style())

    for i, val in enumerate(values):
        for j in range(len(val)):
            sheet1.write(i + 1, j, val[j])


if __name__ == '__main__':
    b = sys.stdin
    title = "DSPID,DSP名称,月份,dealID,deal名称,请求数,DSP参与数,ADX参与数,曝光量,点击量"
    # 将所有的数据放到一个map中，key为pid，value是一个sheet
    all_data = {}
    for ln in b:
        split = ln.split()
        if split[1] not in all_data:
            all_data[split[1]] = []
        all_data[split[1]].append(split)
    # 创建工作簿
    excelFile = xlwt.Workbook(encoding='utf-8')

    for key, val in all_data.items():
        write_excel(excelFile, key, title.split(','), val)

    excelFile.save(str(datetime.date.today()) + "_data.xls")
