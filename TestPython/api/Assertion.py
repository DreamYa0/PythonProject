# -*- coding: utf-8 -*-
"""
所有用例的断言判断
"""
import unittest
from TestPython.api.trip_replay import trip_post
class tripApiTest(unittest.TestCase):
    """replaytrip 轨迹回放"""
    def test_tripSuccuss(self):
        result=trip_post.tripSuccuss()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')
    def test_tripIDNone(self):
        result = trip_post.tripIDNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')
