# -*- coding : utf-8 -*-

import requests
import json

cookieUrl = "http://www-alpha.mycloudhawk.com/api/v1/login"
data = {"username": "zhouyang@supeq.com", "password": "123456"}
Cookies = requests.post(url=cookieUrl, data=json.dumps(data)).cookies
# print(Cookies)