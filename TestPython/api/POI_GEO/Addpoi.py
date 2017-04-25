# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

poisUrl = "/api/v1/pois"
type = "post"
cookie = Mycookies.Cookies


# 无cookie
def AddpoiNocookie():
    data = {"name": "我没有cookie", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 100, "latitude": 110081604.65467232, "longitude": 374620385.14282227, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data)


# 创建poi
def AddpoiSuccess():
    data = {"name": "我成功了", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 100, "latitude": 110081204.65467232, "longitude": 374620386.14282227, "enter_alert": 1,
            "out_alert": 1, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 创建poi不开启提醒
def AddpoiSuccessNoalert():
    data = {"name": "我没有提醒", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 100, "latitude": 110091604.65467232, "longitude": 374620391.14282227, "enter_alert": 0,
            "out_alert": 0, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 名称为空
def AddpoiNameEmpty():
    data = {"name": "", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 100, "latitude": 110041604.65467232, "longitude": 374621385.14282227, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 地址为空
def AddpoiARSEmpty():
    data = {"name": "地址为空", "address": "",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 100, "latitude": 110041611, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为空
def AddpoiPathEmpty():
    data = {"name": "头像为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "",
            "radius": 500, "latitude": 110041604, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径为空
def AddpoiREmpty():
    data = {"name": "半径为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": "", "latitude": 110041604, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度为空
def AddpoiLtEmpty():
    data = {"name": "纬度为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 500, "latitude": "", "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度为空
def AddpoiLgEmpty():
    data = {"name": "经度为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 500, "latitude": 110041609, "longitude": "", "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为空
def AddpoiEAEmpty():
    data = {"name": "进入提醒为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": "", "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为空
def AddpoiOAEmpty():
    data = {"name": "离开提醒为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/user/U000002123.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": "",
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为空
def AddpoitidsEmpty():
    data = {"name": "tid为空", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ""}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 名称为None
def AddpoiNameNone():
    data = {"name": None, "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 地址为None
def AddpoiARSNone():
    data = {"name": "地址为none", "address": None,
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息为None
def AddpoiPathNone():
    data = {"name": "头像信息为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": None,
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径为None
def AddpoiRNone():
    data = {"name": "半径为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": None, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度为None
def AddpoiLtNone():
    data = {"name": "纬度为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": None, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度为None
def AddpoiLgNone():
    data = {"name": "经度为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": None, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为None
def AddpoiEANone():
    data = {"name": "进入提醒为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": None, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为None
def AddpoiOANone():
    data = {"name": "离开提醒为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": None,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# tid为None
def AddpoitidsNone():
    data = {"name": "tid为None", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": None}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# name字段缺失
def AddpoiNoname():
    data = {"address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 地址字段缺失
def AddpoiNoaddress():
    data = {"name": "地址字段缺失", "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 500, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 头像信息字段缺失
def AddpoiNoAP():
    data = {"name": "头像信息字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径字段缺失
def AddpoiNoR():
    data = {"name": "半径字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度字段缺失
def AddpoiNoLT():
    data = {"name": "纬度字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度字段缺失
def AddpoiNoLG():
    data = {"name": "经度字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒字段缺失
def AddpoiNoaEA():
    data = {"name": "进入提醒字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒字段缺失
def AddpoiNoOA():
    data = {"name": "离开提醒字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# poi关联的终端字段缺失
def AddpoiNoTids():
    data = {"name": "poi关联的终端字段缺失", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# name值为int类型
def AddpoiNameInt():
    data = {"name": 711, "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 半径为字符串类型
def AddpoiRStr():
    data = {"name": "半径为字符串类型", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": "500", "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 纬度为字符串类型
def AddpoiLtStr():
    data = {"name": "纬度为字符串类型", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": "81976019", "longitude": 405988769, "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 经度为字符串类型
def AddpoiLgStr():
    data = {"name": "111", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": "405988769", "enter_alert": 1, "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 进入提醒为字符串类型
def AddpoiEAStr():
    data = {"name": "进入提醒为字符串类型", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": "1", "out_alert": 1,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)


# 离开提醒为字符串类型
def AddpoiOAStr():
    data = {"name": "离开提醒为字符串类型", "address": "Jin Shang Xi Yi Lu, Wuhou Qu, Chengdu Shi, Sichuan Sheng, China",
            "avatar_path": "https://s3-ap-southeast-1.amazonaws.com/ch-static-alpha/avatar/poi/g8wq1al51482715489.png",
            "radius": 100, "latitude": 81976019, "longitude": 405988769, "enter_alert": 1, "out_alert": "1",
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(poisUrl, type, data, cookie)
