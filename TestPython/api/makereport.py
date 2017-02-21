# coding = utf-8

"""
生成测试报告
"""

from TestPython.api import TestSuite
import HTMLTestRunner

if __name__ == '__main__':
    filePath = 'F:\CHApiTestReport.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='CloudHawk接口测试报告', description='CloudHawk的登录登出，子账户，角色，poi，围栏，重置密码接口测试报告')
    runner.run(TestSuite.Suite())
    fp.close()
