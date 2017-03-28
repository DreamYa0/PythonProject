# -*- coding: utf-8 -*-

"""
Author:Monica
"""

from TestPython.python_Excel.readExcel import readExcel
from TestPython.python_Excel.testApi import testApi
import unittest
from TestPython.python_Excel import Cookies
import json

excel = readExcel('e:/ch-test.xlsx')
name = excel.getName
url = excel.getUrl
data = excel.getData
method = excel.getMethod
code = excel.getCode
massage = excel.getMessage
token = excel.gettoken
# 获取行数
row = excel.getRows


# 登录
class testLoginApi(unittest.TestCase):
    def test_LoginApi(self):

        # for i in range(0, row - 1):
        #     if token[i] == 0:
        #         api = testApi(method[i], url[i], data[i], Cookies.Cookies)
        #         results = api.getCode()
        #         http_status_code = results.status_code
        #         if http_status_code == 200:
        #             apicode = results.json()['status']
        #             apijson = results.json()['message']
        #             if apicode != int(code[i]) or apijson != massage[i]:
        #                 print('{}、{}:测试失败.json数据为:{}'.format(i + 1, name[i], apijson))
        #         else:
        #             print(results)
        #
        #     else:
        #         api = testApi(method[i], url[i], data[i])
        #         results = api.getCode()
        #         http_status_code = results.status_code
        #         if http_status_code == 200:
        #             apicode = results.json()['status']
        #             apijson = results.json()['message']
        #             if apicode != int(code[i]) or apijson != massage[i]:
        #                 print('{}、{}:测试失败.json数据为:{}'.format(i + 1, name[i], apijson))
        #         else:
        #             print(results)

        for i in range(0, 10):
            if token[i] == 1:
                api = testApi(method[i], url[i], data[i], Cookies.Cookies)
                apicode = api.getCode()
                apijson = api.getJson()
                if apicode != int(code[i]) or apijson != massage[i]:
                    print('{}、{}:测试失败.json数据为:{}'.format(i + 1, name[i], apijson))
            else:
                api = testApi(method[i], url[i], data[i])
                apicode = api.getCode()
                apijson = api.getJson()
                if apicode != int(code[i]) or apijson != massage[i]:
                    print('{}、{}:测试失败.json数据为:{}'.format(i + 1, name[i], apijson))


# 子账户增删查改
class testUsersApi(unittest.TestCase):
    def test_UsersApi(self):
        for i in range(11, row - 1):
            if token[i] == 1:
                api = testApi(method[i], url[i], data[i], Cookies.Cookies)
                apicode = api.getCode()
                apijson = api.getJson()
                if apicode != int(code[i]) or apijson != massage[i]:
                    print('{}、{}:测试失败.message为:{}'.format(i + 1, name[i], apijson))
            else:
                api = testApi(method[i], url[i], data[i])
                apicode = api.getCode()
                apijson = api.getJson()
                if apicode != int(code[i]) or apijson != massage[i]:
                    print('{}、{}:测试失败.message为:{}'.format(i + 1, name[i], apijson))


if __name__ == '__main__':
    unittest.main(verbosity=2)
