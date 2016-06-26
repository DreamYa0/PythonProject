# -*- coding: UTF-8 -*-
# 让字典保存有序切化为Json格式
from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
print(json.dumps(d))  # 序列化为Json格式
