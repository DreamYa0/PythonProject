# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

resetUrl = "/api/v1/reset/password"
type = "put"


# 激活码失效
def resetInvalid():
    data = {"confirmation": "pya66Cp6NvJ7VbMVAN4jcGOUFDakBsAYYIiUI5DaOh9fpKiILHGkiVpi4FFxhVCu", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 错误的激活码
def resetWrongCF():
    data = {"confirmation": "11rN09OGP", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)

# # 密码包含特殊字符
# def resetPwdIllegal():
#     data = {"password": "1*&@|111"}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 激活码为None
# def resetCFNone():
#     data = {"confirmation": None}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码为None
# def resetPwdNone():
#     data = data = { "password": None}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 激活码为空
# def resetCFEmpty():
#     data = {"confirmation": ""}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码为空
# def resetPwdEmpty():
#     data = { "password": ""}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码值为一位
# def resetPwdless():
#     data = {"password": "1"}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码值为6位
# def resetPwdMin():
#     data = { "password": "111111"}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码值为20位
# def resetPwdMax():
#     data = {"password": "11111111111111111111"}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码值为21位
# def resetPwdOut():
#     data = {"password": "111111111111111111111"}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 密码为int类型
# def resetPwdInt():
#     data = {"password": 111111}
#     return ApiMethod.testMethod(resetUrl, type, data)
#
#
# # 重置密码成功
# def resetSuccess():
#     data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA", "password": "111111"}
#     return ApiMethod.testMethod(resetUrl, type, data)
