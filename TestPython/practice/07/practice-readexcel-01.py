# -*- coding: utf-8 -*-

"""
Author:monica
"""

import xlrd
# import json


def open_excel(file='e:/ch-test.xlsx'):         # 构造函数，打开文件
    try:
        data = xlrd.open_workbook(file)         # 尝试打开文件读取数据
        return data
    except Exception as e:
        print(str(e))


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径    colnameindex：表头列名所在行的索引  ，by_index：表的索引
def excel_table_byindex(file='e:/ch-test.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]             # 技巧讲解table = data.sheets()[0]  通过索引顺序获取
    nrows = table.nrows                         # 获取行数
    # ncols = table.ncols                       # 获取列数
    colnames = table.row_values(colnameindex)   # table.row_values(i)， table.col_values(i)获取整行和整列的值（数组）
    apps = []
    for rownum in range(1, nrows):              # 循环行列表数据
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            apps.append(app)
    return apps


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def excel_table_byname(file='e:/ch-test.xlsx', colnameindex=0, by_name=None):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)   # 某一行数据
    apps = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            apps.append(app)
    return apps


def main():
    tables = excel_table_byindex()
    for row in tables:
        print(row)

    tables = excel_table_byname()
    for row in tables:
        print(row)

    if __name__ == "__main__":
        main()