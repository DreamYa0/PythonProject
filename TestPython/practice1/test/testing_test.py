# coding=utf-8
from TestPython.practice1.test.testing_readingExcel import readExcel
from TestPython.practice1.test import testing_testApi
import unittest

excel = readExcel('e:/test-ch.xls')
name = excel.getName
url = excel.getUrl
data = excel.getData
method = excel.getMethod
code = excel.getCode
body = excel.getBody
token = excel.gettoken
# 获取行数
row = excel.getRows


class testLoginApi1(unittest.TestCase):
    def test_LoginApi1(self):
        for i in range(0, row - 1):
            api = testing_testApi.testApi(method[i], url[i], data[i])
            apicode = api.getCode()
            apijson = api.getJson()
            if apicode != int(code[i]) or apijson != body[i]:
                print('{}、{}:测试失败.json数据为:{},{}'.format(i + 1, name[i], apicode, apijson))
            else:
                print("{}、{}:测试通过.json数据为：{},{}".format(i + 1, name[i], apicode, apijson))


if __name__ == '__main__':
    unittest.main(verbosity=2)
