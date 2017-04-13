# -*- coding: utf-8 -*-

"""
Author:Monica
"""

from TestPython.python_Excel.readExcel import readExcel
from TestPython.python_Excel.testApi import testApi
from TestPython.python_Excel import asserttool
import json
from TestPython.python_Excel import test

result = test.testLoginApi().test_LoginApi
code = test.testLoginApi().code
message = test.testLoginApi().message


class TestLogin:
    def test0(self):
        asserttool.Asserttool(result[0], code[0], message[0])

    def test1(self):
        asserttool.Asserttool(result[1], code[1], message[1])

    def test2(self):
        asserttool.Asserttool(result[2], code[2], message[2])

    def test3(self):
        asserttool.Asserttool(result[3], code[3], message[3])

    def test4(self):
        asserttool.Asserttool(result[4], code[4], message[4])

    def test5(self):
        asserttool.Asserttool(result[5], code[5], message[5])

    def test6(self):
        asserttool.Asserttool(result[6], code[6], message[6])

    def test7(self):
        asserttool.Asserttool(result[7], code[7], message[7])

    def test8(self):
        asserttool.Asserttool(result[8], code[8], message[8])

    def test9(self):
        asserttool.Asserttool(result[9], code[9], message[9])
