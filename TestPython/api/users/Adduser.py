# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl = "/api/v1/users"
type = "post"
cookie = Mycookies.Cookies


# 无权限新增子账号
def AdduserNoCookie():
    data = {"email": "a1@qq.com", "first_name": "one", "last_name": "a1", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1101, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data)


# 成功新增子账号
def AdduserSuccess():
    data = {"email": "a32@qq.com", "first_name": "one", "last_name": "a32", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1132, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱为None
def AdduserENone():
    data = {"email": None, "first_name": "ying", "last_name": "a2", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1102, "tids": ["898602B12616C0613882", "89860042191586153394"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为None
def AdduserFNNONE():
    data = {"email": "a3@qq.com", "first_name": None, "last_name": "a3", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1103, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为None
def AdduserLNNone():
    data = {"email": "a4@qq.com", "first_name": "one", "last_name": None, "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1104, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为None
def AdduserATNone():
    data = {"email": "a5@qq.com", "first_name": "one", "last_name": "a5", "week": None, "phone": "123456",
            "password": "123456", "role_id": 1105, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为None
def AdduserMNone():
    data = {"email": "a6@qq.com", "first_name": "one", "last_name": "a6", "week": "1111111", "phone": None,
            "password": "123456", "role_id": 1106, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码为None
def AdduserPwdNone():
    data = {"email": "a7@qq.com", "first_name": "one", "last_name": "a7", "week": "1111111", "phone": "123456",
            "password": None, "role_id": 1107, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为None
def AdduserRIdNone():
    data = {"email": "a8@qq.com", "first_name": "one", "last_name": "a8", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": None, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为None
def AdduserTidsNone():
    data = {"email": "a9@qq.com", "first_name": "one", "last_name": "a9", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1109, "tids": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱为空
def AdduserEEmpty():
    data = {"email": "", "first_name": "one", "last_name": "a10", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1101, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为空
def AdduserFNEmpty():
    data = {"email": "a11@qq.com", "first_name": "", "last_name": "a11", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1111, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为空
def AdduserLNEmpty():
    data = {"email": "a12@qq.com", "first_name": "one", "last_name": "", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1112, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为空
def AdduserATEmpty():
    data = {"email": "a13@qq.com", "first_name": "one", "last_name": "a13", "week": "", "phone": "123456",
            "password": "123456", "role_id": 1113, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为空
def AdduserMEmpty():
    data = {"email": "a14@qq.com", "first_name": "one", "last_name": "a14", "week": "1111111", "phone": "",
            "password": "123456", "role_id": 1114, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码为空
def AdduserPwdEmpty():
    data = {"email": "a15@qq.com", "first_name": "one", "last_name": "a15", "week": "1111111", "phone": "123456",
            "password": "", "role_id": 1115, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为空
def AdduserRIdEmpty():
    data = {"email": "a16@qq.com", "first_name": "one", "last_name": "a16", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": "", "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为空
def AdduserTidsEmpty():
    data = {"email": "a17@qq.com", "first_name": "one", "last_name": "a17", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1117, "tids": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱字段缺失
def AdduserNoEmail():
    data = {"first_name": "one", "last_name": "a18", "week": "1111111", "phone": "123456", "password": "123456",
            "role_id": 1118, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段缺失
def AdduserNoFN():
    data = {"email": "a19@qq.com", "last_name": "a19", "week": "1111111", "phone": "123456", "password": "123456",
            "role_id": 1119, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段缺失
def AdduserNoLN():
    data = {"email": "a20@qq.com", "first_name": "one", "week": "1111111", "phone": "123456", "password": "123456",
            "role_id": 1120, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间字段缺失
def AdduserNoAT():
    data = {"email": "a21@qq.com", "first_name": "one", "last_name": "a21", "phone": "123456", "password": "123456",
            "role_id": 1121, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段缺失
def AdduserNoM():
    data = {"email": "a22@qq.com", "first_name": "one", "last_name": "a22", "week": "1111111", "password": "123456",
            "role_id": 1122, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码字段缺失
def AdduserNoPwd():
    data = {"email": "a23@qq.com", "first_name": "one", "last_name": "a23", "week": "1111111", "phone": "123456",
            "role_id": 1123, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id字段缺失
def AdduserNoRId():
    data = {"email": "a24@qq.com", "first_name": "one", "last_name": "a24", "week": "1111111", "phone": "123456",
            "password": "123456", "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids字段缺失
def AdduserNoTids():
    data = {"email": "a25@qq.com", "first_name": "one", "last_name": "a25", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1125}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-主账号邮箱
def AdduserAEmailError():
    data = {"email": "zhouyang@supeq.com", "first_name": "one", "last_name": "a26", "week": "1111111",
            "phone": "123456", "password": "123456", "role_id": 1126, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-子账号邮箱
def AdduserUEmailError():
    data = {"email": "a32@qq.com", "first_name": "one", "last_name": "a27", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1127, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱错误-邮箱格式非法
def AdduserEFormError():
    data = {"email": "49819", "first_name": "one", "last_name": "a28", "week": "1111111", "phone": "123456",
            "password": "123456", "role_id": 1128, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度小于6位
def AdduserPwdLess():
    data = {"email": "a29@qq.com", "first_name": "one", "last_name": "a29", "week": "1111111", "phone": "1234",
            "password": "123456", "role_id": 1129, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度等于20位
def AdduserPwdMax():
    data = {"email": "a30@qq.com", "first_name": "one", "last_name": "a30", "week": "1111111",
            "phone": "12345678910123456789", "password": "123456", "role_id": 1130, "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度大于20位
def AdduserPwdOut():
    data = {"email": "a31@qq.com", "first_name": "one", "last_name": "a31", "week": "1111111",
            "phone": "12345612345678910123456789", "password": "123456", "role_id": 1131,
            "tids": ["898602B12616C0613882"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)
