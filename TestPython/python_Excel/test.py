# -*- coding: utf-8 -*-

"""
Author:Monica
"""

from TestPython.python_Excel.readExcel import readExcel
from TestPython.python_Excel.testApi import testApi
import unittest
import logging
from TestPython.python_Excel import Cookies
import json
from TestPython.python_Excel import Readsheet

logging.basicConfig(level=logging.INFO)
excel = readExcel('e:/ch-test.xlsx')


# 模块名
class testLoginApi:
    def __init__(self):
        self.sheet1 = excel.getSheet[0]
        excel.getName = self.sheet1
        self.name = excel.getName
        excel.getUrl = self.sheet1
        self.url = excel.getUrl
        excel.getData = self.sheet1
        self.data = excel.getData
        excel.getMethod = self.sheet1
        self.method = excel.getMethod
        excel.getCode = self.sheet1
        self.code = excel.getCode
        excel.getMessage = self.sheet1
        self.message = excel.getMessage
        excel.gettoken = self.sheet1
        self.token = excel.gettoken
        # 获取行数
        excel.getRows = self.sheet1
        self.row = excel.getRows

    def test_LoginApi(self):
        TextResult = []
        for i in range(0, self.row - 1):
            if self.token[i] == 0:
                api = testApi(self.method[i], self.url[i], self.data[i]).testApi
                if api.status_code == 200:
                    TextResult.append(api)
                else:
                    logging.info(self.method[i] + ',' + self.data[i])
        return TextResult


class testRoleApi:
    def __init__(self):
        self.sheet1 = excel.getSheet[1]
        excel.getName = self.sheet1
        self.name = excel.getName
        excel.getUrl = self.sheet1
        self.url = excel.getUrl
        excel.getData = self.sheet1
        self.data = excel.getData
        excel.getMethod = self.sheet1
        self.method = excel.getMethod
        excel.getCode = self.sheet1
        self.code = excel.getCode
        excel.getMessage = self.sheet1
        self.message = excel.getMessage
        excel.gettoken = self.sheet1
        self.token = excel.gettoken
        # 获取行数
        excel.getRows = self.sheet1
        self.row = excel.getRows

    def test_RoleApi(self):
        TextResult = []
        for i in range(0, self.row - 1):
            if self.token[i] == 0:
                api = testApi(self.method[i], self.url[i], self.data[i]).testApi
                if api.status_code == 200:
                    TextResult.append(api)
                else:
                    logging.info(self.method[i] + ',' + self.data[i])
        return TextResult
print(testLoginApi().test_LoginApi())
print(testRoleApi().test_RoleApi())

# apicode = api.getCode()
# apijson = api.getJson()
#     if apicode != int(code[i]) or apijson != massage[i]:
#         print('{}、{}:测试失败.json数据为:{},{}'.format(i + 1, name[i], apicode, apijson))
# else:
#     api = testApi(method[i], url[i], data[i])
#     apicode = api.getCode()
#     apijson = api.getJson()
#     if apicode != int(code[i]) or apijson != massage[i]:
#         print('{}、{}:测试失败.json数据为:{},{}'.format(i + 1, name[i], apicode, apijson))


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
