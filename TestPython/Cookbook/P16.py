a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
print(a.keys() & b.keys())  # 找出两个集合键相同的项
print(a.keys() - b.keys())  # 找出两个集合中不相同的项
print(a.items() & b.items())  # 找出两个集合中键和值相同的项
