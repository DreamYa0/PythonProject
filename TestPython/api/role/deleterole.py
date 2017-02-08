# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

roleUrl = "/api/v1/roles/1103"
type = "delete"
cookie = Mycookies.Cookies


# 无cookie
def roleNocookie():
    return ApiMethod.testMethod(roleUrl, type, None)


# 成功删除子角色
def roleDeleteSuccess():
    return ApiMethod.testMethod(roleUrl, type, None, cookie)
