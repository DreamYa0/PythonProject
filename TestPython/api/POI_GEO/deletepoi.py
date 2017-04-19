# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.POI_GEO import pois


poisUrl = "/api/v1/pois/560"
type = "delete"
cookie = Mycookies.Cookies


# 没有Cookie
def deletePoiNocookie():
    return ApiMethod.testMethod(poisUrl, type, None)


# 成功删除poi
def deletePoiSuccess():
    return ApiMethod.testMethod(poisUrl, type, None, cookie)
