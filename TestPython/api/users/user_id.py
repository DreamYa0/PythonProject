# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.users import userManagement


user_id=str(userManagement.userSuccess()['data'][0]['id'])
print(user_id)
userUrl = "/api/v1/users/"+user_id
type = "get"
cookie = Mycookies.Cookies


# 获取单个子账号详情
def oneuserSuccess():
    return ApiMethod.testMethod(userUrl, type, None, cookie)


# 没有获取权限
def oneuserNocookie():
    return ApiMethod.testMethod(userUrl, type, None)
