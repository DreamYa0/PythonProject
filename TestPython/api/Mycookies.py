# -*- coding: utf-8 -*-
"""
保存cookie
"""
import requests
import json

cookieUrl = "http://192.168.3.149:8080/api/v1/login"
data = {'username': 'zhouyang@supeq.com', 'password': '123456'}
Cookies = requests.post(url=cookieUrl, data=json.dumps(data)).cookies
