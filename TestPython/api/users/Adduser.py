# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl = "/api/v1/users"
type = "post"
cookie = Mycookies.Cookies


# 无权限新增子账号
def AdduserNoCookie():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data)


# 成功新增子账号
def AdduserSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)

# 邮箱为None
def AdduserENone():
    data = {"email": None, "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为None
def AdduserFNNONE():
    data = {"email": "49819@qq.com", "first_name": None, "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为None
def AdduserLNNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": None, "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为None
def AdduserATNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": None, "phone": "123456",
            "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为None
def AdduserMNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": None, "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码为None
def AdduserPwdNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": None, "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为None
def AdduserRIdNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": None, "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为None
def AdduserTidsNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱为空
def AdduserEEmpty():
    data = {"email": "", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为空
def AdduserFNEmpty():
    data = {"email": "49819@qq.com", "first_name": "", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为空
def AdduserLNEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为空
def AdduserATEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": "", "phone": "123456",
            "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为空
def AdduserMEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码为空
def AdduserPwdEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为空
def AdduserRIdEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为空
def AdduserTidsEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱字段缺失
def AdduserNoEmail():
    data = {"first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6], "phone": "123456",
            "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段缺失
def AdduserNoFN():
    data = {"email": "49819@qq.com", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6], "phone": "123456",
            "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段缺失
def AdduserNoLN():
    data = {"email": "49819@qq.com", "first_name": "ying", "week": [0, 1, 2, 3, 4, 5, 6], "phone": "123456",
            "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间字段缺失
def AdduserNoAT():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "phone": "123456", "password": "123456",
            "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段缺失
def AdduserNoM():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码字段缺失
def AdduserNoPwd():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id字段缺失
def AdduserNoRId():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids字段缺失
def AdduserNoTids():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-主账号邮箱
def AdduserAEmailError():
    data = {"email": "zhouyang@supeq.com", "first_name": "ying", "last_name": "tao",
            "week": [0, 1, 2, 3, 4, 5, 6], "phone": "123456", "password": "123456", "role_id": "531",
            "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-子账号邮箱
def AdduserUEmailError():
    data = {"email": "3097944@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱错误-邮箱格式非法
def AdduserEFormError():
    data = {"email": "zhouyang", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段字符长度大于20位
def AdduserFNBig():
    data = {"email": "49819@qq.com", "first_name": "AAAAAAAAAAAAAAAAAAAA", "last_name": "tao",
            "week": [0, 1, 2, 3, 4, 5, 6], "phone": "123456", "password": "123456", "role_id": "531",
            "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段长度大于20位
def AdduserLNBig():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "AAAAAAAAAAAAAAAAAAAAA",
            "week": [0, 1, 2, 3, 4, 5, 6], "phone": "123456", "password": "123456", "role_id": "531",
            "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段长度大于50位
def AdduserMEBig():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "111111111111111111111111111111111111111111111111112", "password": "123456", "role_id": "531",
            "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度大于20位
def AdduserPwdBig():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456777777777777778", "role_id": "531",
            "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度小于6位
def AdduserPwdSmall():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "12345", "password": "1234", "role_id": "531", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id不存在
def AdduserRIdError():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "week": [0, 1, 2, 3, 4, 5, 6],
            "phone": "123456", "password": "123456", "role_id": "4", "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)
