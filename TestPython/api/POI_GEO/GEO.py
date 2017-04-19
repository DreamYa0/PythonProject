# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

geoUrl = "/api/v1/regions"
type = "get"
cookie = Mycookies.Cookies


# 无Cookie进行获取
def geoNocookie():
    data = {"page": 1}
    return ApiMethod.testMethod(geoUrl, type, data)


# 获取geo列表
def geoSuccess():
    data = {"page": 1}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 当前页为空
def geoEmpty():
    data = {"page": ""}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 当前页为None
def geoNone():
    data = {"page": None}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 每页显示条数为None
def geoPSizaNone():
    data = {"page": 1, "page_size": None}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# page为字符串
def geoStr():
    data = {"page": "jk"}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# page_size为字符串
def geoPSStr():
    data = {"page": 1, "page_size": "fg"}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)
