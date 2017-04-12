# -*- coding: utf-8 -*-

"""
Author:Monica
"""

from TestPython.python_Excel.readExcel import readExcel
from TestPython.python_Excel.testApi import testApi
import unittest
import logging
from TestPython.python_Excel import monica
import json
from TestPython.python_Excel import test


# def Monica(result, code, message):
#     assert result['status'] == code
#     assert result['message'] == message

result = test.testLoginApi().test_LoginApi
code = test.testLoginApi().code
message = test.testLoginApi().message


class TestLogin:
    def test0(self):
        monica.Monica(result[0], code[0], message[0])

    def test1(self):
        pass
        # for i in range(0, test.testLoginApi().row-1):
        #         ttttt(result, i, code)
        # assert result[0]['status'] == code[0]
        # assert result[1]['status'] == code[1]
        # assert result[2]['status'] == code[2]
        # assert result[3]['status'] == code[3]
        # assert result[4]['status'] == code[4]
        # assert result[5]['status'] == code[5]
        # assert result[6]['status'] == code[6]
        # assert result[7]['status'] == code[7]
        # assert result[8]['status'] == code[8]
        # assert result[9]['status'] == code[9]

    # def testMessage(self):
    #     result = test.testLoginApi().test_LoginApi
    #     message = test.testLoginApi().message
    #     assert result[0]['message'] == message[0]
    #     assert result[1]['message'] == message[1]
    #     assert result[2]['message'] == message[2]
    #     assert result[3]['message'] == message[3]
    #     assert result[5]['message'] == message[5]
    #     assert result[6]['message'] == message[6]
    #     assert result[7]['message'] == message[7]
    #     assert result[8]['message'] == message[8]
    #     assert result[9]['message'] == message[9]
