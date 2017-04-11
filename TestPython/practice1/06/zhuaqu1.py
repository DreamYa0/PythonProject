# -*- coding:utf-8 -*-
import urllib.request

url = 'http://www.yttx.co/custom/login.htm?action=enter'  # 访问登录页面进行爬虫
webPage = urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
