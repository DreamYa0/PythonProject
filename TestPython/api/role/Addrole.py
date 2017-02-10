# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

roleUrl = "/api/v1/roles"
type = "post"
cookie = Mycookies.Cookies


# 创建子角色
def addroleSuccess():
    data = {"name": "lala", "permissions": [6, 1, 4, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 无权限创建角色
def addroleNocookie():
    data = {"name": "lala", "permissions": [6, 1, 4, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data)


# name唯一性检测
def addroleOnly():
    data = {"name": "lala", "permissions": [6, 1, 4, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# name为空
def addroleNMEmpty():
    data = {"name": "", "permissions": [6, 1, 4, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 权限为空
def addrolePMSEmpty():
    data = {"name": "lala", "permissions": ""}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# name为None
def addroleNMNone():
    data = {"name": None, "permissions": ""}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 权限为None
def addrolePMSNone():
    data = {"name": "lala", "permissions": None}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# name字段缺失
def addroleNoNM():
    data = {"permissions": ""}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 权限字段缺失
def addroleNoPMS():
    data = {"name": "lala"}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# name为int类型
def addroleNMInt():
    data = {"name": 456, "permissions": [6, 1, 4, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 权限为字符串
def addrolePMSStr():
    data = {"name": "lala", "permissions": "[6, 1, 4, 3, 5, 2]"}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)
