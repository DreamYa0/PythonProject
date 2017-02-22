# -*- coding: utf-8 -*-
"""
所有用例的断言判断
"""
import unittest
from TestPython.api.common import code


class codeApiTest(unittest.TestCase):
    """生成激活码"""

    def test_codeSNEmpty(self):
        result = code.codeSNEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_codeiccidEmpty(self):
        result = code.codeiccidEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_codeSNNone(self):
        result = code.codeSNNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_codeiccidNone(self):
        result = code.codeiccidNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_codeSNNo(self):
        result = code.codeSNNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_codeiccidNo(self):
        result = code.codeSNNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_codeSuccess(self):
        result = code.codeSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')
