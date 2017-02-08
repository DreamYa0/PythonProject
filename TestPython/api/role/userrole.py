# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

roleUrl = "/api/v1/roles"
type = "get"
cookie = Mycookies.Cookies


# 获取权限子账号的信息
def userroleSuccess():
    return ApiMethod.testMethod(roleUrl, type, None, cookie)


# 无权限获取
def userroleNocookie():
    return ApiMethod.testMethod(roleUrl, type, None)
