# coding = utf-8

"""
生成测试报告
"""

from TestPython.api import TestSuite
import HTMLTestRunner

if __name__ == '__main__':
    filePath = 'F:\CHApiTestReport.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='CloudHawk接口测试报告', description='CloudHawk的注册，用户信息，终端信息，修改邮箱，标签接口测试报告')
    runner.run(TestSuite.Suite())
    fp.close()
