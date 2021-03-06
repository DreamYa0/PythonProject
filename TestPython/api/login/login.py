# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

loginUrl = "/api/v1/login"
type = 'post'


# 正确的用户名
def loginSuccess():
    data = {"username": "zhouyang@supeq.com", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名或密码错误
def loginUserErrorOrPwdError():
    data = {"username": "21gh23654@qq.com", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名未激活
def loginNoActive():
    data = {"username": "wefaw@qqfq.com", "password": "123456"}
    return ApiMethod.testMethod(loginUrl, type, data)


# 用户名为none
def loginUserNone():
    data = {"username": None, "password": "123456"}
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
