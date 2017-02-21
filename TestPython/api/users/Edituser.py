# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl = "/api/v1/users/309794415@qq.com"
type = "put"
cookie = Mycookies.Cookies


# 无权限修改子账号
def EdituserNoCookie():
    data = {"email": "309794415@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "role_id": 1079, "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data)


# 邮箱为None
def EdituserENone():
    data = {"email": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为None
def EdituserFNNONE():
    data = {"first_name": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为None
def EdituserLNNone():
    data = {"last_name": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为None
def EdituserATNone():
    data = {"week": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为None
def EdituserMNone():
    data = {"phone": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为None
def EdituserRIdNone():
    data = {"role_id": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为None
def EdituserTidsNone():
    data = {"tids": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱为空
def EdituserEEmpty():
    data = {"email": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为空
def EdituserFNEmpty():
    data = {"first_name": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为空
def EdituserLNEmpty():
    data = {"last_name": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为空
def EdituserATEmpty():
    data = {"week": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为空
def EdituserMEmpty():
    data = {"phone": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为空
def EdituserRIdEmpty():
    data = {"role_id": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为空
def EdituserTidsEmpty():
    data = {"tids": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-主账号邮箱
def EdituserAEmailError():
    data = {"email": "zhouyang@supeq.com"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-子账号邮箱
def EdituserUEmailError():
    data = {"email": "3097944@qq.com"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱错误-邮箱格式非法
def EdituserEFormError():
    data = {"email": "zhouyang"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段字符长度大于20位
def EdituseFNMax():
    data = {"first_name": "AAAAAAAAAAAAAAAAAAAA"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段长度大于20位
def EdituserLNMax():
    data = {"last_name": "AAAAAAAAAAAAAAAAAAAAA"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段长度大于50位
def EdituserMEMax():
    data = {"phone": "111111111111111111111111111111111111111111111111112"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id不存在
def EdituserRIdError():
    data = {"tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱修改成功
def EdituserESuccess():
    data = {"email": "4981844@qq.com"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名修改成功
def EdituserFNSuccess():
    data = {"first_name": "zhou"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓修改成功
def EdituserLNSuccess():
    data = {"last_name": "yang"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间修改成功
def EdituserATSuccess():
    data = {"week": [0, 1, 2, 3]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话修改成功
def EdituserMSuccess():
    data = {"phone": "12345678"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id修改成功
def EdituserRIdSuccess():
    data = {"role_id": "532"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids修改成功
def EdituserTidsSuccess():
    data = {"tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)
