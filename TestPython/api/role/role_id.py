# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies


roleUrl = "/api/v1/roles/1105"
type = "get"
cookie = Mycookies.Cookies


# 获取单个子角色信息
def oneroleSuccess():
    return ApiMethod.testMethod(roleUrl, type, None, cookie)


# 无权限获取信息
def oneroleNocookie():
    return ApiMethod.testMethod(roleUrl, type, None)
