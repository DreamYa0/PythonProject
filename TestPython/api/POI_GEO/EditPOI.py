# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.POI_GEO import pois

poi_id = str(pois.poisSuccess()['data'][0]['id'])
poisUrl = "/api/v1/pois/"+poi_id
type = "put"
cookie = Mycookies.Cookies


# 无cookie
def EditPOINocookie():
    data = {"name": "111",
            "avatar_path": "/static/icons/poi/default.png",
            "enter_alert": 1, "out_alert": 1, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data)

print(EditPOINocookie())

# 修改poi名称
def EditPOINameSuccess():
    data = {"name": "222"}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改头像信息
def EditPOIAPSuccess():
    data = {"avatar_path": "/static/icons/poi/default.1478767996762.png", }
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改进入提醒
def EditPOIEASuccess():
    data = {"enter_alert": 0}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改离开提醒
def EditPOIOASuccess():
    data = {"out_alert": 0}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改关联终端
def EditPOITidsSuccess():
    data = {"tids": ["89860042191586153394"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# poi名称为空
def EditPOINameEmpty():
    data = {"name": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为空
def EditPOIPathEmpty():
    data = {"avatar_path": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为空
def EditPOIEAEmpty():
    data = {"enter_alert": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为空
def EditPOIOAEmpty():
    data = {"out_alert": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为空
def EditPOItidsEmpty():
    data = {"tids": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 名称为None
def EditPOINameNone():
    data = {"name": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为None
def EditPOIPathNone():
    data = {"avatar_path": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为None
def EditPOIEANone():
    data = {"enter_alert": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为None
def EditPOIOANone():
    data = {"out_alert": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为None
def EditPOItidsNone():
    data = {"tids": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改Poi名称为int类型
def EditPOINameInt():
    data = {"name": 555}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改进入提醒值为字符串
def EditPOIEAStr():
    data = {"enter_alert": "1"}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改离开提醒值为字符串
def EditPOIOAStr():
    data = {"out_alert": "1"}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 修改为不存在的关联终端
def EditPOITidsNoExist():
    data = {"tids": ["89302720396911547656"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)
