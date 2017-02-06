# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl = "/api/v1/admin/user"
type = "get"
cookie = Mycookies.Cookies


# 获取子账号
def userSuccess():
    return ApiMethod.testMethod(userUrl, type, None, cookie)


# 无权限获取子账号
def userNoCookie():
    return ApiMethod.testMethod(userUrl, type, None)
