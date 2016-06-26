# -*- coding: UTF-8 -*-

# 从序列中移除重复项且保持元素间顺序不变


def depupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(depupe(a)))
