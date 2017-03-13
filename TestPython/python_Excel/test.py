# -*- coding: utf-8 -*-

"""
Author:Monica
"""

from TestPython.python_Excel.readExcel import readExcel
from TestPython.python_Excel.testApi import testApi
import unittest


class testLoginApi(unittest.TestCase):
    def test_LoginApi(self):

        excel = readExcel('e:/ch-test.xlsx')
        name = excel.getName
        url = excel.getUrl
        data = excel.getData
        method = excel.getMethod
        code = excel.getCode
        massage=excel.getMessage
        row = excel.getRows
        print(name)
        print(url)
        print(data)
        print(method)
        print(code)
        print(massage)
        for i in range(0, row - 1):
            api = testApi(method[i], url[i], data[i])
            apicode = api.getCode()
            apijson = api.getJson()
            try:
                self.assertEqual(apijson['status'], int(code[i]))
            except:
                pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
