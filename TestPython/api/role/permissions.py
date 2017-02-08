# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

roleUrl = "/api/v1/roles/permissions"
type = "get"
cookie = Mycookies.Cookies


# 获取角色的所有权限
def roleSuccess():
    return ApiMethod.testMethod(roleUrl, type, None, cookie)


# 无权限获取
def roleNocookie():
    return ApiMethod.testMethod(roleUrl, type, None)
