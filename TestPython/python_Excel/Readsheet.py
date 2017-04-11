# coding=utf-8
from TestPython.python_Excel.readExcel import readExcel

excel = readExcel('e:/ch-test.xlsx')


class ReadSheet:
    def __init__(self):

        self.sheet = excel.getSheet()
        self.name = excel.getName
        self.url = excel.getUrl
        self.data = excel.getData
        self.method = excel.getMethod
        self.code = excel.getCode
        self.message = excel.getMessage
        self.token = excel.gettoken
        self.row = excel.getRows
        excel.getName = self.sheet
        excel.getUrl = self.sheet
        excel.getData = self.sheet
        excel.getMethod = self.sheet
        excel.getCode = self.sheet
        excel.getMessage = self.sheet
        excel.gettoken = self.sheet
        excel.getRows = self.sheet
