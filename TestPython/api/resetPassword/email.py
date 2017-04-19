# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

resetUrl = "/api/v1/reset/password"
type = "get"


# 已注册未激活的邮箱
def resetUnregistered():
    data = {"email": "afewf@geawfw.com"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 邮箱名为None
def resetNone():
    data = {"email": None}
    return ApiMethod.testMethod(resetUrl, type, data)


# 邮箱名为空
def resetEmpty():
    data = {"email": ""}
    return ApiMethod.testMethod(resetUrl, type, data)


# 邮箱非法格式
def resetInvalidFormat():
    data = {"email": "498194410"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 未注册的邮箱
def resetNotfound():
    data = {"email": "zxcvb@qq.com"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 字段缺失(不传参)
def resetNoEmail():
    return ApiMethod.testMethod(resetUrl, type)


# 正确的邮箱
def resetSuccess():
    data = {"email": "3097944154@qq.com"}
    return ApiMethod.testMethod(resetUrl, type, data)
