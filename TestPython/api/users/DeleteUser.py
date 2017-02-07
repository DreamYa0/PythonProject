# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl = "/api/v1/users/309794415@qq.com"
type = "delete"
cookie = Mycookies.Cookies


# 删除子账号
def deleteUserSuccess():
    return ApiMethod.testMethod(userUrl, type, None, cookie)


# 无权限删除子账号
def deleteUserNocookie():
    return ApiMethod.testMethod(userUrl, type, None)
