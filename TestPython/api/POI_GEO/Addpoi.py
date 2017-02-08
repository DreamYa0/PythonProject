# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

poisUrl = "/api/v1/pois"
type = "post"
cookie = Mycookies.Cookies


# 无cookie
def AddpoiNocookie():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data)


# 创建poi
def AddpoiSuccess():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 名称为空
def AddpoiNameEmpty():
    data = {"name": "", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 地址为空
def AddpoiARSEmpty():
    data = {"name": "111", "address": "",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为空
def AddpoiPathEmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径为空
def AddpoiREmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": "", "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度为空
def AddpoiLtEmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": "", "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度为空
def AddpoiLgEmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": "", "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为空
def AddpoiEAEmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": "", "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为空
def AddpoiOAEmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": "",
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为空
def AddpoitidsEmpty():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 名称为None
def AddpoiNameNone():
    data = {"name": None, "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 地址为None
def AddpoiARSNone():
    data = {"name": "111", "address": None,
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为None
def AddpoiPathNone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": None,
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径为None
def AddpoiRNone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": None, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度为None
def AddpoiLtNone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": None, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度为None
def AddpoiLgNone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": None, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为None
def AddpoiEANone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": None, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为None
def AddpoiOANone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": None,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为None
def AddpoitidsNone():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# name字段缺失
def AddpoiNoname():
    data = {"address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 地址字段缺失
def AddpoiNoaddress():
    data = {"name": "111", "avatar_path": "https://s3.amazonaws.com/tm-static-alpha/avatar/poi"
                                          "/e7f4eb548cfa11e6a0b902012bcdef411475891994.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息字段缺失
def AddpoiNoAP():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径字段缺失
def AddpoiNoR():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度字段缺失
def AddpoiNoLT():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度字段缺失
def AddpoiNoLG():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒字段缺失
def AddpoiNoaEA():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒字段缺失
def AddpoiNoOA():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# poi关联的终端
def AddpoiNoTids():
    data = {"name": "111", "address": "中国四川省成都市青羊区青羊宫商圈牧电巷59号 邮政编码: 610041",
            "avatar_path": "/static/icons/poi/default.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)
