# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

notificationUrl = "/api/v1/trackers/898602B12616C0613882/notifications"
type = "put"
cookie = Mycookies.Cookies


# 无cookie
def notificationNocookie():
    data = {"stopping": 0}
    return ApiMethod.testMethod(notificationUrl, type, data)


