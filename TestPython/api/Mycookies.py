# -*- coding: utf-8 -*-
"""
保存cookie
"""
import requests
import json

cookieUrl = "http://www-alpha.mycloudhawk.com/api/v1/login"
data1 = {'username': 'zhouyang@supeq.com', 'password': '123456'}
data2 = {'username': 'zhouyang@supeq.com', 'password': '123456'}
data3 = {'username': 'zhouyang@supeq.com', 'password': '11111111111111111111'}
Cookies = requests.post(url=cookieUrl, data=json.dumps(data1)).cookies


def cookie(data):
    return requests.post(url=cookieUrl, data=json.dumps(data)).cookies
