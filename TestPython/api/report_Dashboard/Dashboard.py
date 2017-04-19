# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

reportUrl = "/api/v1/report/dashboard"
type = "get"
cookie = Mycookies.Cookies


# 获得各类报表前7天数据排序信息

# 获取mileage报表行驶距离前7数据
def mileageSuccess():
    data = {"r_type": 1}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取driving time报表行驶时间前7数据
def driving_timeSuccess():
    data = {"r_type": 2}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取fuel报表油耗前7数据
def fuelSuccess():
    data = {"r_type": 3}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取speed报表平均速度前7数据
def speedSuccess():
    data = {"r_type": 4}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取temperature报表终端平均温度前7数据
def temperatureSuccess():
    data = {"r_type": 5}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取POI/GEO Visit报表触发次数前7数据
def visitSuccess():
    data = {"r_type": 6}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取maintence报表车辆剩余保养距离/车辆剩余保养时间前7数据
def maintenceSuccess():
    data = {"r_type": 7}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 获取IFTA Fuel Tax Mileage报表所有车辆在州行驶距离总和前7数据
def IFIASuccess():
    data = {"r_type": 8}
    return ApiMethod.testMethod(reportUrl, type, data, cookie)


# 无权限查询任意报表前7数据
def NOcookie():
    data = {"r_type": 1}
    return ApiMethod.testMethod(reportUrl, type, data)
