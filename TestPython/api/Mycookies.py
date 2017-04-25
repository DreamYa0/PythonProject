# -*- coding: utf-8 -*-
"""
保存cookie
"""
import requests
import json

cookieUrl = "http://www-alpha.mycloudhawk.com/api/v1/login"
data1 = {'username': 'zhouyang@supeq.com', 'password': '123456'}

Cookies = requests.post(url=cookieUrl, data=json.dumps(data1)).cookies

# data2 = {'username': 'zhouyang@supeq.com', 'password': '123456'}
# data3 = {'username': 'zhouyang@supeq.com', 'password': '11111111111111111111'}
# def cookie(data=None):
#     kookie = json.dumps(data2)
#     resp = requests.post(url=cookieUrl, data=kookie)
#     cookies = resp.cookies
#     username = data2.get("username")
#     # 从文件中加载json
#     old_cookies = json.load(open("cookies.json"))
#     cookie_v = cookies.values()
#     old_cookies[username] = cookie_v[0] if cookie_v else ""
#     with open("cookies.json", "w") as f:
#         # 把json转换成字符串，每行缩进2个空格
#         s_cookies = json.dumps(cookies, indent=2)
#         # 写入并保存文件
#         f.write(json.dumps(cookies, indent=2))
