# -*- coding: utf-8 -*-
"""
保存cookie
"""
import requests
import json

cookieUrl = "http://www-alpha.mycloudhawk.com/login"
data = {'username':'zhouyang@supeq.com','password':'123456'}
header = {'Content-Type':'application/x-www-form-urlencoded'}
# 也可以不要header
Cookies = requests.post(url=cookieUrl,data = data,headers = header).cookies
