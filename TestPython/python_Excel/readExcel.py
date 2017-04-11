# -*- coding: utf-8 -*-

"""
Author:Monica
"""

import xlrd


class readExcel(object):
    def __init__(self, path: object):
        self.path = path

    @property  # 把方法变成属性可以直接进行调用,只有@property表示只读
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheets()
        return sheet

    @property
    def getRows(self):
        # 获取行数
        row = self.sheet.nrows
        return row

    @getRows.setter         # 有@property and @x.setter表示可读可写;同时有@property和@x.setter和@x.deleter表示可读可写可删除。
    def getRows(self, sheet):
        self.sheet = sheet

    @property
    def getCol(self):
        # 获取列数
        col = self.sheet.ncols
        return col

    @getCol.setter
    def getCol(self, sheet):
        self.sheet = sheet

    # 以下是分别获取每一列的数值
    @property
    def getName(self):
        TextName = []
        for i in range(1, self.getRows):
            TextName.append(self.sheet.cell_value(i, 0))  # append() 方法向列表的尾部添加一个新的元素。只接受一个参数。
        return TextName

    @getName.setter
    def getName(self, sheet):
        self.sheet = sheet

    @property
    def getUrl(self):
        TextUrl = []
        for i in range(1, self.getRows):
            TextUrl.append(self.sheet.cell_value(i, 1))
        return TextUrl

    @getUrl.setter
    def getUrl(self, sheet):
        self.sheet = sheet

    @property
    def getData(self):
        TextData = []
        for i in range(1, self.getRows):
            TextData.append(self.sheet.cell_value(i, 2))
        return TextData

    @getData.setter
    def getData(self, sheet):
        self.sheet = sheet

    @property
    def getMethod(self):
        TextMethod = []
        for i in range(1, self.getRows):
            TextMethod.append(self.sheet.cell_value(i, 3))
        return TextMethod

    @getMethod.setter
    def getMethod(self, sheet):
        self.sheet = sheet

    @property
    def getCode(self):
        TextCode = []
        for i in range(1, self.getRows):
            TextCode.append(self.sheet.cell_value(i, 4))
        return TextCode

    @getCode.setter
    def getCode(self, sheet):
        self.sheet = sheet

    @property
    def getMessage(self):
        TextMessage = []
        for i in range(1, self.getRows):
            TextMessage.append(self.sheet.cell_value(i, 5))
        return TextMessage

    @getMessage.setter
    def getMessage(self, sheet):
        self.sheet = sheet

    @property
    def gettoken(self):
        Texttoken = []
        for i in range(1, self.getRows):
            Texttoken.append(self.sheet.cell_value(i, 6))
        return Texttoken

    @gettoken.setter
    def gettoken(self, sheet):
        self.sheet = sheet
