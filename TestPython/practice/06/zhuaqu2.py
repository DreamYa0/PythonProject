# -*- coding:utf-8 -*-
import urllib.request

weburl = 'http://www.yttx.co/custom/login.htm?action=enter'
webheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}  # 模仿一个浏览器
req = urllib.request.Request(url=weburl, headers=webheader)
webPage = urllib.request.urlopen(req)
date = webPage.read()
date = date.decode('utf-8')
print(date)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
