# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

loginUrl = "/api/v1/login"
type = 'post'


# 正确的用户名
def loginSuccess():
    data = {"username": "zhouyang@supeq.com", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名或密码不存在
def loginUserErrorOrPwdError():
    data = {"username": "498194@qq.com", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名未激活
def loginNoActive():
    data = {"username": "498194410@qq.com", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名为none
def loginUserNone():
    data = {"username": None, "password": 123456}
    return ApiMethod.testMethod(loginUrl, type, data)


# 密码为none
def loginPwdNone():
    data = {"username": "zhouyang@supeq.com", "password": None}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名为空
def loginUserEmpty():
    data = {"username": "", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 密码为空
def loginPwdEmpty():
    data = {"username": "zhouyang@supeq.com", "password": ""}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名字段缺失
def loginNoUser():
    data = {"password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 密码字段缺失
def loginNoPwd():
    data = {"username": "zhouyang@supeq.com"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 密码小于6位
def loginPwdSmall():
    data = {"username": "zhouyang@supeq.com", "password": "12345"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 密码大于20位
def loginPwdBig():
    data = {"username": "zhouyang@supeq.com", "password": "111111111111111111111"}
    return ApiMethod.testMethod(loginUrl, type, data)
