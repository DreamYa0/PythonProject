# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod

codeUrl = "/api/v1/activationcode"
type = "get"


# sn为空
def codeSNEmpty():
    data = {"sn": "", "iccid": "898602B12616C0614231"}
    return ApiMethod.testMethod(codeUrl, type, data)


# iccid为空
def codeiccidEmpty():
    data = {"sn": "0000022077", "iccid": ""}
    return ApiMethod.testMethod(codeUrl, type, data)


# sn为None
def codeSNNone():
    data = {"sn": None, "iccid": "898602B12616C0614231"}
    return ApiMethod.testMethod(codeUrl, type, data)


# iccid为None
def codeiccidNone():
    data = {"sn": "0000022077", "iccid": None}
    return ApiMethod.testMethod(codeUrl, type, data)


# sn字段缺失
def codeSNNo():
    data = {"iccid": "898602B12616C0614231"}
    return ApiMethod.testMethod(codeUrl, type, data)


# iccid字段缺失
def codeiccidNo():
    data = {"sn": "0000022077"}
    return ApiMethod.testMethod(codeUrl, type, data)


# 通过sn和iccid获取激活码
def codeSuccess():
    data = {"sn": "3E428007AF", "iccid": "898602B12616C0613882"}
    return ApiMethod.testMethod(codeUrl, type, data)
