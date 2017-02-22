# coding = utf-8

'''
此文件为测试套件
'''
import unittest
from TestPython.api.common import Assertion


def suite():
    suite = unittest.TestSuite()
    # 获取激活码
    suite.addTest(Assertion.codeApiTest("test_codeSNEmpty"))
    suite.addTest(Assertion.codeApiTest("test_codeiccidEmpty"))
    suite.addTest(Assertion.codeApiTest("test_codeSNNone"))
    suite.addTest(Assertion.codeApiTest("test_codeiccidNone"))
    suite.addTest(Assertion.codeApiTest("test_codeSNNo"))
    suite.addTest(Assertion.codeApiTest("test_codeiccidNo"))
    suite.addTest(Assertion.codeApiTest("test_codeSuccess"))
    return suite

print(suite())