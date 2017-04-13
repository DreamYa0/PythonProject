# -*- coding: utf-8 -*-

"""
Author:Monica
"""


def Asserttool(result, code, message):
    assert result['status'] == code
    assert result['message'] == message
