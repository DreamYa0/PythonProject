# -*- coding: UTF-8 -*-
import urllib.request  # 把这两个库导入

url = 'https://api.douban.com/v2/book/user/ahbei/collections'  # 这是要请求的url
data = {'status': 'read', 'rating': 3, 'tag': '小说'}  # 根据api文档提供的参数，我们来获取一下阿北读过的书中，他标记了‘小说’这个标签的三星书籍，把这些参数值存在一个dict里
data = urllib.parse.urlencode(data)  # 把参数进行编码
url2 = urllib.request.Request(url+'?'+data)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
response = urllib.request.urlopen(url2)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
apicontent = response.read()  # 将响应内容用read()读取出来
print(apicontent)  # 打印读取到的内容


