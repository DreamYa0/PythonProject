# -*- coding: utf-8 -*-

"""
Author:Monica
"""
import requests
import json
# from pubulic_way.get_token import get_token


class testApi(object):
    def __init__(self, method, url, data, cookies=None):
        self.method = method
        self.url = url
        self.data = data
        self.cookies = cookies

    @property
    def testApi(self):
        try:
            r = None
            url = self.url
            data = json.loads(self.data)
            if self.method == 'post':
                r = requests.post(url, json=data, cookies=self.cookies)
            elif self.method == 'get':
                r = requests.get(url, params=data,cookies=self.cookies)
            elif self.method == 'put':
                r = requests.put(url, json=data,cookies=self.cookies)
            elif self.method == 'delete':
                r = requests.delete(url, json=data,cookies=self.cookies)
            return r
        except Exception as e:
            print(e.args)

    def getCode(self):
        # 获取访问接口的状态码
        if self.testApi.status_code == 200:
            result = self.testApi.json()['status']
            return result

    def getJson(self):
        # 获取返回信息的json数据
        json_data = self.testApi.json()['message']
        return json_data
