# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl = "/api/v1/users/309794415@qq.com"
type = "put"
cookie = Mycookies.Cookies


# 无权限修改子账号
def AdituserNoCookie():
    data = {"email": "309794415@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data)


# 邮箱为None
def AdituserENone():
    data = {"email": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为None
def AdituserFNNONE():
    data = {"first_name": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为None
def AdituserLNNone():
    data = {"last_name": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为None
def AdituserATNone():
    data = {"week": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为None
def AdituserMNone():
    data = {"phone": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为None
def AdituserRIdNone():
    data = {"role_id": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为None
def AdituserTidsNone():
    data = {"tids": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱为空
def AdituserEEmpty():
    data = {"email": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为空
def AdituserFNEmpty():
    data = {"first_name": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为空
def AdituserLNEmpty():
    data = {"last_name": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为空
def AdituserATEmpty():
    data = {"week": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为空
def AdituserMEmpty():
    data = {"phone": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为空
def AdituserRIdEmpty():
    data = {"role_id": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为空
def AdituserTidsEmpty():
    data = {"tids": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-主账号邮箱
def AdituserAEmailError():
    data = {"email": "zhouyang@supeq.com"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-子账号邮箱
def AdituserUEmailError():
    data = {"email": "3097944@qq.com"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱错误-邮箱格式非法
def AdituserEFormError():
    data = {"email": "zhouyang"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段字符长度大于20位
def AdituserFNBig():
    data = {"first_name": "AAAAAAAAAAAAAAAAAAAA"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段长度大于20位
def AdituserLNBig():
    data = {"last_name": "AAAAAAAAAAAAAAAAAAAAA"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段长度大于50位
def AdituserMEBig():
    data = {"phone": "111111111111111111111111111111111111111111111111112"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id不存在
def AdituserRIdError():
    data = {"tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱修改成功
def AdituserESuccess():
    data = {"email": "4981844@qq.com"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名修改成功
def AdituserFNSuccess():
    data = {"first_name": "zhou"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓修改成功
def AdituserLNSuccess():
    data = {"last_name": "yang"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间修改成功
def AdituserATSuccess():
    data = {"week": [0, 1, 2, 3]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话修改成功
def AdituserMSuccess():
    data = {"phone": "12345678"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id修改成功
def AdituserRIdSuccess():
    data = {"role_id": "532"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids修改成功
def AdituserTidsSuccess():
    data = {"tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)
