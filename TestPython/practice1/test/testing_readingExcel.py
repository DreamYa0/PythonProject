# -*- cooding:utf-8 -*-
import xlrd


class readExcel():
    def __init__(self, path):
        self.path = path

    @property
    def getsheet(self):
        book = xlrd.open_workbook(self.path)
        sheet = book.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        row = self.getsheet.nrows
        return row

    @property
    def getCols(self):
        col = self.getsheet.ncols
        return col

    @property
    def getName(self):
        TextName = []
        for i in range(1, self.getRows):
            TextName.append(self.getsheet.cell_value(i, 0))
        return TextName

    @property
    def getUrl(self):
        TextUrl = []
        for i in range(1, self.getRows):
            TextUrl.append(self.getsheet.cell_value(i, 1))
        return TextUrl

    @property
    def getData(self):
        TextData = []
        for i in range(1, self.getRows):
            TextData.append(self.getsheet.cell_value(i, 2))
        return TextData

    @property
    def getMethod(self):
        TextMethod = []
        for i in range(1, self.getRows):
            TextMethod.append(self.getsheet.cell_value(i, 3))
        return TextMethod

    @property
    def getCode(self):
        TextCode = []
        for i in range(1, self.getRows):
            TextCode.append(self.getsheet.cell_value(i, 4))
        return TextCode

    @property
    def getBody(self):
        TextBody = []
        for i in range(1, self.getRows):
            TextBody.append(self.getsheet.cell_value(i, 5))
        return TextBody

    @property
    def gettoken(self):
        Texttoken = []
        for i in range(1, self.getRows):
            Texttoken.append(self.getsheet.cell_value(i, 6))
        return Texttoken
