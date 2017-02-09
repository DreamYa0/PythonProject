# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.POI_GEO import pois


poi_id=str(pois.poisSuccess()['data'][0]['id'])
poisUrl = " /api/v1/pois/"+poi_id
type = "delete"
cookie = Mycookies.Cookies


# 没有Cookie
def deletePoiNocookie():
    return ApiMethod.testMethod(poisUrl, type, None)


# 成功删除poi
def deletePoiSuccess():
    return ApiMethod.testMethod(poisUrl, type, None, cookie)
