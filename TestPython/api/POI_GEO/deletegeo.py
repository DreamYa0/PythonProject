# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

regionEditUrl = "/api/v1/regions/1746"
type = "delete"
cookie = Mycookies.Cookies


# 无cookie
def deletegeoNocookie():
    return ApiMethod.testMethod(regionEditUrl, type, None)


# 删除围栏
def deletegeoSuccess():
    return ApiMethod.testMethod(regionEditUrl, type, None, cookie)
