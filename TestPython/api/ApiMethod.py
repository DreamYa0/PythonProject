# -*- coding: utf-8 -*-
"""
请求方法的封装
"""
# 调用哪个模块--定义地址变量--定义调用的请求方法
import requests
import json
# 定义地址变量
base_url = "www-alpha.mycloudhawk.com"
# 根据type来判断调用哪种请求方法
def testMethod(url,type,data = None,cookie = None):
    if type == "get" :
        return requests.get(url = base_url + url,params = data ,cookies = cookie ).json()
    elif type == "post":
        return requests.post(url =base_url + url ,data= json.dumps(data),cookies=cookie).json()
        # post方法的body部分是字典类型，此处data是将字典类型转化为json格式
    elif type == "put":
        return requests.put(url=base_url + url,data=json.dumps(data),cookies=cookie).json()
    elif type == "delete":
        return requests.delete(url=base_url + url,cookies=cookie).json()