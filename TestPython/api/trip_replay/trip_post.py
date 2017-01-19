# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

tripUrl = "api/vi/trip"
# 功能描述：获取查询时间范围内终端轨迹详细信息
type = "post"
cookie = Mycookies.Cookies


# 成功查询轨迹
def tripSuccuss():
    data = {"start_time": 1478016000, "end_time": 1478102399, "id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl, type, data)


# id值为None
def tripIDNone():
    data = {"start_time": 1478016000, "end_time": 1478102399, "id": None}
    return ApiMethod.testMethod(tripUrl, type, data)


# 开始时间为None
def tripSTNone():
    data = {"start_time": None, "end_time": 1478102399, "id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl, type, data, )


# 结束时间值为None
def tripETNone():
    data = {"start_time": 1478016000, "end_time": None, "id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl, type, data)


# id为空
def tripIdEmpty():
    data = {"start_time": 1478016000, "end_time": 1478102399, "id": ""}
    return ApiMethod.testMethod(tripUrl, type, data)


# 开始时间值为空
def tripSTEmpty():
    data = {"start_time": "", "end_time": 1478102399, "id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl, type, data)


# 结束时间值为空
def tripETEmpty():
    data = {"start_time": 1478016000, "end_time": "", "id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl, type, data)


# id字段缺失
def tripNoID():
    data = {"start_time": 1478016000, "end_time": 1478102399, }
    return ApiMethod.testMethod(tripUrl, type, data)


# 开始时间字段缺失
def tripNoST():
    data={"end_time": 1478102399, "id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl,type,data)

# 结束字段缺失
def tripNoET():
    data = {"start_time": 1478016000,"id": "898602B12616C0613882"}
    return ApiMethod.testMethod(tripUrl,type,data)
