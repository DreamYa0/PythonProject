# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

userUrl ="/api/v1/admin/user:id"
type = "put"
cookie = Mycookies.Cookies


# 无权限修改子账号
def AdituserNoCookie():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data)
# 邮箱为None
def AdituserENone():
    data = {"email": None, "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为None
def AdituserFNNONE():
    data = {"email": "49819@qq.com", "first_name": None, "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为None
def AdituserLNNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": None, "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为None
def AdituserATNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": None, "mobile": "123456",
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为None
def AdituserMNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": None, "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码为None
def AdituserPwdNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": None, "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为None
def AdituserRIdNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": None, "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为None
def AdituserTidsNone():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": None}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱为空
def AdituserEEmpty():
    data = {"email": "", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名为空
def AdituserFNEmpty():
    data = {"email": "49819@qq.com", "first_name": "", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓为空
def AdituserLNEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间为空
def AdituserATEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": "", "mobile": "123456",
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为空
def AdituserMEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码为空
def AdituserPwdEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id为空
def AdituserRIdEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids为空
def AdituserTidsEmpty():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ""}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱字段缺失
def AdituserNoEmail():
    data = {"first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6], "mobile": "123456",
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段缺失
def AdituserNoFN():
    data = {"email": "49819@qq.com", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6], "mobile": "123456",
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段缺失
def AdituserNoLN():
    data = {"email": "49819@qq.com", "first_name": "ying", "allow_time": [0, 1, 2, 3, 4, 5, 6], "mobile": "123456",
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间字段缺失
def AdituserNoAT():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "mobile": "123456", "password": "123456",
            "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段缺失
def AdituserNoM():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码字段缺失
def AdituserNoPwd():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id字段缺失
def AdituserNoRId():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids字段缺失
def AdituserNoTids():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531"}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-主账号邮箱
def AdituserAEmailError():
    data = {"email": "zhouyang@supeq.com", "first_name": "ying", "last_name": "tao",
            "allow_time": [0, 1, 2, 3, 4, 5, 6], "mobile": "123456", "password": "123456", "role_id": "531",
            "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱唯一性-子账号邮箱
def AdituserUEmailError():
    data = {"email": "3097944@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 邮箱错误-邮箱格式非法
def AdituserEFormError():
    data = {"email": "zhouyang", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名字段字符长度大于20位
def AdituserFNBig():
    data = {"email": "49819@qq.com", "first_name": "AAAAAAAAAAAAAAAAAAAA", "last_name": "tao",
            "allow_time": [0, 1, 2, 3, 4, 5, 6], "mobile": "123456", "password": "123456", "role_id": "531",
            "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓字段长度大于20位
def AdituserLNBig():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "AAAAAAAAAAAAAAAAAAAAA",
            "allow_time": [0, 1, 2, 3, 4, 5, 6], "mobile": "123456", "password": "123456", "role_id": "531",
            "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话字段长度大于50位
def AdituserMEBig():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "111111111111111111111111111111111111111111111111112", "password": "123456", "role_id": "531",
            "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度大于20位
def AdituserPwdBig():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456777777777777778", "role_id": "531",
            "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码长度小于6位
def AdituserPwdSmall():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "12345", "password": "1234", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id不存在
def AdituserRIdError():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "4", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)
# 邮箱修改成功
def AdituserESuccess():
    data = {"email": "4981844@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 名修改成功
def AdituserFNSuccess():
    data = {"email": "49819@qq.com", "first_name": "zhou", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 姓修改成功
def AdituserLNSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "yang", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 允许时间修改成功
def AdituserATSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0,1,2,3], "mobile": "123456",
            "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 电话为空
def AdituserMSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "12345678", "password": "123456", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 密码修改成功
def AdituserPwdSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "111111", "role_id": "531", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# 角色id修改成功
def AdituserRIdSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "532", "tids": ["3E428007AF", "3728800381"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)


# tids修改成功
def AdituserTidsSuccess():
    data = {"email": "49819@qq.com", "first_name": "ying", "last_name": "tao", "allow_time": [0, 1, 2, 3, 4, 5, 6],
            "mobile": "123456", "password": "123456", "role_id": "531", "tids": ["3E428007AF"]}
    return ApiMethod.testMethod(userUrl, type, data, cookie)