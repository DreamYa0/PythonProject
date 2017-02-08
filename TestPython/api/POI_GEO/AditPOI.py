# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

poisUrl = " /api/v1/pois/523"
type = "put"
cookie = Mycookies.Cookies


# 无cookie
def AditpoiNocookie():
    data = {"name": "111",
            "avatar_path": "/static/icons/poi/default.png",
            "enter_alert": 1, "out_alert": 1, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data)


# 修改poi名称
def AditpoiNameSuccess():
    data = {"name": "222"}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改头像信息
def AditpoiAPSuccess():
    data = {"avatar_path": "/static/icons/poi/default.1478767996762.png", }
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改进入提醒
def AditpoiEASuccess():
    data = {"enter_alert": 0}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改离开提醒
def AditpoiOASuccess():
    data = {"out_alert": 0}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改关联终端
def AditpoiTidsSuccess():
    data = {"tids": ["89860042191586153394"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# poi名称为空
def AditpoiNameEmpty():
    data = {"name": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为空
def AditpoiPathEmpty():
    data = {"avatar_path": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为空
def AditpoiEAEmpty():
    data = {"enter_alert": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为空
def AditpoiOAEmpty():
    data = {"out_alert": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为空
def AditpoitidsEmpty():
    data = {"tids": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 名称为None
def AditpoiNameNone():
    data = {"name": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为None
def AditpoiPathNone():
    data = {"avatar_path": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为None
def AditpoiEANone():
    data = {"enter_alert": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为None
def AditpoiOANone():
    data = {"out_alert": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为None
def AditpoitidsNone():
    data = {"tids": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)
