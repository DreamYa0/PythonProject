# -*- coding: UTF-8 -*-
# 与字典有关的计算问题
prices = {'AECM': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
min_price = min(zip(prices.values(), prices.keys()))  # 找出最小价格
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))  # 找出最大价格
print(max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))  # 对价格排序
print(prices_sorted)
