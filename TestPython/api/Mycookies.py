# -*- coding: utf-8 -*-
"""
保存cookie
"""
import requests
import json

cookieUrl = "www-alpha.mycloudhawk.com/login"
data = {"username":"zhouyang@supeq.com","password":"123456"}
Cookies = requests.post(url=cookieUrl,data = json.dumps(data)).cookies
