# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

poisUrl = "/api/v1/pois"
type = "get"
cookie = Mycookies.Cookies


# 无Cookie进行获取
def poisNocookie():
    data = {"page": 1, "page_size": 20}
    return ApiMethod.testMethod(poisUrl, type, data)


# 获取poi列表
def poisSuccess():
    data = {"page": 1, "page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 当前页数字段缺失
def poisNoPage():
    data = {"page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 每页显示条数字段缺失
def poisNoPSiza():
    data = {"page": 1}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 当前页为空
def poisEmpty():
    data = {"page": "", "page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 每页显示条数为空
def poisPSizaEmpty():
    data = {"page": 1, "page_size": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 当前页为None
def poisNone():
    data = {"page": None, "page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 每页显示条数为None
def poisPSizaNone():
    data = {"page": 1, "page_size": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# page为字符串
def poisStr():
    data = {"page": "1", "page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# page_size为字符串
def poisPSStr():
    data = {"page": 1, "page_size": "10"}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# page值不存在
def poisPageNoExist():
    data = {"page": 0, "page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# page_size值不存在
def poisPSizeNoExist():
    data = {"page": 0, "page_size": 10}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)
