# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

notificationUrl = "/api/v1/trackers/898602B12616C0613882/notifications"
type = "get"
cookie = Mycookies.Cookies


# 无cookie
def notificationNocookie():
    return ApiMethod.testMethod(notificationUrl, type, None)


# 获取标签列表
def notificationSuccess():
    return ApiMethod.testMethod(notificationUrl, type, None, cookie)
