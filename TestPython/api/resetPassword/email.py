# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

resetUrl = "/api/v1/password"
type = "get"


# 正确的邮箱
def resetSuccess():
    data = {"email": "zhouyang@supeq.com"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 已注册未激活的邮箱
def resetUnregistered():
    data = {"email": "498194410@qq.com"}
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
    data = {"email": "952659830@qq.com"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 字段缺失
def resetNoEmail():
    return ApiMethod.testMethod(resetUrl, type)
