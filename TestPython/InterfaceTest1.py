import urllib.request
import json


def http_post():
    url = 'http://192.168.1.13:9999/test'
    values = "{\'user\':\'Smith\',\'passwd\':123456}"

    jdata = json.dumps(values)  # 对数据进行JSON格式化编码
    req = urllib.request.Request(url+'?'+jdata)  # 生成页面请求的完整数据
    response = urllib.request.urlopen(req)  # 发送页面请求
    return response.read()  # 获取服务器返回的页面信息
    resp = http_post()
    print(resp)
