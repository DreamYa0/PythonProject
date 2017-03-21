# -*- coding: utf-8 -*-

"""
Author:Monica
"""

import xlrd


class readExcel(object):
    def __init__(self, path: object):
        self.path = path

    @property  # 把方法变成属性可以直接进行调用
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        # 获取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCol(self):
        # 获取列数
        col = self.getSheet.ncols
        return col

    # 以下是分别获取每一列的数值
    @property
    def getName(self):
        TextName = []
        for i in range(1, self.getRows):
            TextName.append(self.getSheet.cell_value(i, 0))
        return TextName

    @property
    def getUrl(self):
        TextUrl = []
        for i in range(1, self.getRows):
            TextUrl.append(self.getSheet.cell_value(i, 1))
        return TextUrl

    @property
    def getData(self):
        TextData = []
        for i in range(1, self.getRows):
            TextData.append(self.getSheet.cell_value(i, 2))
        return TextData

    @property
    def getMethod(self):
        TextMethod = []
        for i in range(1, self.getRows):
            TextMethod.append(self.getSheet.cell_value(i, 3))
        return TextMethod

    @property
    def getCode(self):
        TextCode = []
        for i in range(1, self.getRows):
            TextCode.append(self.getSheet.cell_value(i, 4))
        return TextCode

    @property
    def getMessage(self):
        TextMessage = []
        for i in range(1, self.getRows):
            TextMessage.append(self.getSheet.cell_value(i, 5))
        return TextMessage

    @property
    def gettoken(self):
        Texttoken = []
        for i in range(1, self.getRows):
            Texttoken.append(self.getSheet.cell_value(i, 6))
        return Texttoken
