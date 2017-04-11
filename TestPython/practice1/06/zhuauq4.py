# 使用request抓取网页
import urllib.request
req = urllib.request.Request('http://www.yttx.co/custom/login.htm?action=enter')
response = urllib.request.urlopen(req)
html = response.read()
html = html.decode('utf-8')
print(html)