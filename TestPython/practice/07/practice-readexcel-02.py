# -*- coding: utf-8 -*-
"""
Author:monica
"""


import xlrd

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook('e:/ch-test.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())
    sheet1_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('Sheet1')

    # sheet的名称，行数，列数
    print(sheet1.name, sheet1.nrows, sheet1.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(3)  # 获取第四行内容
    cols = sheet1.col_values(2)  # 获取第三列内容
    print(rows)
    print(cols)

    # 获取单元格内容
    print(sheet1.cell(1, 0).value.encode('utf-8'))
    print(sheet1.cell_value(1, 0).encode('utf-8'))
    print(sheet1.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    print(sheet1.cell(1, 0).ctype)

if __name__ == '__main__':
    read_excel()