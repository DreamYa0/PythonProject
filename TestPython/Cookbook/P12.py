# -*- coding: UTF-8 -*-

from collections import defaultdict
# 在字典中将键值映射到多个值上
d = defaultdict(list)
d['a'].append(1)
d['c'].append(2)
d['b'].append(4)
print(d)
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
