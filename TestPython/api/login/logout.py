# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

logoutUrl = "/api/v1/logout"
type = "get"
cookie = Mycookies.Cookies


# 登出失败
def logoutFail():
    return ApiMethod.testMethod(logoutUrl, type)


# 成功登出
def logoutSuccess():
    return ApiMethod.testMethod(logoutUrl, type, None, cookie)
