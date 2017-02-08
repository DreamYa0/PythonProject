# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

geoUrl = "/api/v1/regions"
type = "get"
cookie = Mycookies.Cookies


# 无Cookie进行获取
def geoNocookie():
    data = {"page": 1, "page_size": 20}
    return ApiMethod.testMethod(geoUrl, type, data)


# 获取poi列表
def geoSuccess():
    data = {"page": 1, "page_size": 10}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 当前页数字段缺失
def geoNoPage():
    data = {"page_size": 10}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 当前页为空
def geoEmpty():
    data = {"page": "", "page_size": 10}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 当前页为None
def geoNone():
    data = {"page": None, "page_size": 10}
    return ApiMethod.testMethod(geoUrl, type, data, cookie)
