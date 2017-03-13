# coding = utf-8

"""
生成测试报告
"""
import unittest

from TestPython.python_Excel import test
import HTMLTestRunner

if __name__ == '__main__':
    filePath = 'F:\CHTestReport.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='CloudHawk接口测试报告', description='CloudHawk的登录登出，子账户，角色，poi，围栏，重置密码接口测试报告')
    suite = unittest.TestSuite()
    suite.addTest(test.testLoginApi("test_LoginApi"))
    runner.run(suite)
    fp.close()
