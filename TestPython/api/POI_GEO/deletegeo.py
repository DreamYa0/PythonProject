# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.POI_GEO import GEO

geo_id = str(GEO.geoSuccess()['data'][0]['id'])
regionEditUrl = "/api/v1/regions/" + geo_id
type = "delete"
cookie = Mycookies.Cookies
#无cookie
def deletegeoNocookie():
    return ApiMethod.testMethod(regionEditUrl,type,None)
# 删除围栏
def deletegeoSuccess():
    return ApiMethod.testMethod(regionEditUrl,type,None,cookie)