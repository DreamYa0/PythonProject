# 最简单的抓取网页
import urllib.request
response = urllib.request.urlopen('http://www.yttx.co/custom/login.htm?action=enter')
html = response.read()
html = html.decode('utf-8')
print(html)