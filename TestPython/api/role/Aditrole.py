# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

roleUrl = "/api/v1/roles/1103"
type = "put"
cookie = Mycookies.Cookies


# 无权限进行修改
def roleNocookie():
    data = {"name": "pro", "permissions": [6, 1, 4, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data)


# 修改角色名称
def rolenameSuccess():
    data = {"name": "aaa"}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 修改角色权限
def rolePMSSuccess():
    data = {"permissions": [6, 3, 5, 2]}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 修改为不存在的角色权限
def rolePMSNothing():
    data = {"permissions": [9, 10, 11]}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 角色名称为None
def rolenameNone():
    data = {"name": None}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 角色权限为None
def rolePMSNone():
    data = {"permissions": None}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 角色名称为空
def rolenameEmpty():
    data = {"name": ""}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)


# 角色权限为空
def rolePMSEmpty():
    data = {"permissions": ""}
    return ApiMethod.testMethod(roleUrl, type, data, cookie)