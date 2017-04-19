# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

timelineUrl = "/api/v1/trip/timeline"
type = "post"
cookie = Mycookies.Cookies


# 没有权限查询
def timelineNoCookie():
    data = {"ids": "898602B12616C0614231", "start_time": 1492531200, "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data)


# 查询单个终端轨迹
def timelineSuccessA():
    data = {"ids": "898602B12616C0614231", "start_time": 1492531200, "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# ids为None
def timelineIdsNone():
    data = {"ids": None, "start_time": 1492531200, "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 开始时间为None
def timelineSTNone():
    data = {"ids": "898602B12616C0613882,89860042191586153394", "start_time": None, "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 结束时间为None
def timelineETNone():
    data = {"ids": "898602B12616C0613882,89860042191586153394", "start_time": 1492531200, "end_time": None}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# ids为空
def timelineIdsEmpty():
    data = {"ids": "", "start_time": 1492531200, "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 开始时间为空
def timelineSTEmpty():
    data = {"ids": "898602B12616C0613882,89860042191586153394", "start_time": "", "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 结束时间为空
def timelineETEmpty():
    data = {"ids": "898602B12616C0613882,89860042191586153394", "start_time": 1492531200, "end_time": ""}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# ids字段缺失
def timelineNoIds():
    data = {"start_time": 1492531200, "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 开始时间字段缺失
def timelineNoST():
    data = {"ids": "898602B12616C0613882,89860042191586153394", "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 结束时间字段缺失
def timelineNoET():
    data = {"ids": "898602B12616C0613882,89860042191586153394", "start_time": 1492531200, }
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 开始时间值为字符串
def timelineSTStr():
    data = {"ids": "898602B12616C0613882", "start_time": "1492531200", "end_time": 1492617599}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)


# 结束时间值为字符串
def timelineETStr():
    data = {"ids": "898602B12616C0613882", "start_time": 1492531200, "end_time": "1492617599"}
    return ApiMethod.testMethod(timelineUrl, type, data, cookie)
