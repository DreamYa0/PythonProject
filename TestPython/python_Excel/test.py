# -*- coding: utf-8 -*-

"""
Author:Monica
"""

from TestPython.python_Excel.readExcel import readExcel
from TestPython.python_Excel.testApi import testApi
import unittest
from TestPython.python_Excel import Cookies
import json


class testLoginApi(unittest.TestCase):
    def test_LoginApi(self):

        excel = readExcel('e:/ch-test.xlsx')
        name = excel.getName
        url = excel.getUrl
        data = excel.getData
        method = excel.getMethod
        code = excel.getCode
        massage = excel.getMessage
        token = excel.gettoken
        row = excel.getRows

        for i in range(0, row - 1):
            if token[i] == 0:
                api = testApi(method[i], url[i], data[i], Cookies.Cookies)
                apicode = api.getCode()
                apijson = api.getJson()
                if apicode != int(code[i]) or apijson != massage[i]:
                    print('{}、{}:测试失败.json数据为:{}'.format(i + 1, name[i], apijson))
                    # print('{}、{}:测试成功'.format(i + 1, name[i]))
            else:
                api = testApi(method[i], url[i], data[i])
                apicode = api.getCode()
                apijson = api.getJson()
                if apicode != int(code[i]) or apijson != massage[i]:
                    print('{}、{}:测试失败.json数据为:{}'.format(i + 1, name[i], apijson))
                    # print('{}、{}:测试成功'.format(i + 1, name[i]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
