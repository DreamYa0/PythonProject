# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

resetUrl = "/api/v1/password"
type = "put"


# 重置密码成功
def resetSuccess():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 激活码失效
def resetInvalid():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 错误的激活码
def resetWrongCF():
    data = {"confirmation": "11rN09OGP", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码包含特殊字符
def resetPwdIllegal():
    data = {"confirmation": "11rN09OGP", "password": "1*&@|111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 激活码为None
def resetCFNone():
    data = {"confirmation": None, "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码为None
def resetPwdNone():
    data = data = {"confirmation": None, "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 激活码为空
def resetCFEmpty():
    data = {"confirmation": "", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码为空
def resetPwdEmpty():
    data = {"confirmation": "", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 激活码字段缺失
def resetNoCF():
    data = {"password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码字段缺失
def resetNoPwd():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码值为一位
def resetPwdless():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA", "password": "1"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码值为6位
def resetPwdMin():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA", "password": "111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码值为20位
def resetPwdMax():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA",
            "password": "11111111111111111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码值为21位
def resetPwdOut():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA",
            "password": "111111111111111111111"}
    return ApiMethod.testMethod(resetUrl, type, data)


# 密码为int类型
def resetPwdInt():
    data = {"confirmation": "11rN09OGPJgHwLFF68JLHiqmL886FWrtx4xKvRdd92NISCvHjXzQKL1gFyl25gqA",
            "password": 111111}
    return ApiMethod.testMethod(resetUrl, type, data)
