# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.role import userrole

role_id=str(userrole.userroleSuccess()['data'][0]['id'])
roleUrl = "/api/v1/roles/"+role_id
type = "delete"
cookie = Mycookies.Cookies


# 无cookie
def roleNocookie():
    return ApiMethod.testMethod(roleUrl, type, None)


# 成功删除子角色
def roleDeleteSuccess():
    return ApiMethod.testMethod(roleUrl, type, None, cookie)
