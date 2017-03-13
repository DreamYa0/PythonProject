# -*- coding: utf-8 -*-

"""
Author:Monica
"""
import requests
import json


# from pubulic_way.get_token import get_token



class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data

    @property
    def testApi(self):
        try:
            r = None
            if self.method == 'post':
                url = self.url
                data = json.loads(self.data)
                r = requests.post(url, json=data)
            elif self.method == 'get':
                r = requests.get(self.url, params=eval(self.data))
            else:
                print('失败')
            return r
        except Exception as e:
            print(e.args)

    def getCode(self):
        # 获取访问接口的状态码
        if self.testApi.status_code == 200:
            result = self.testApi.json()
            return result

    def getJson(self):
        # 获取返回信息的json数据
        json_data = self.testApi.json()
        return json_data
