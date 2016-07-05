"""
def 函数名（参数列表）：
    函数体
"""


# 求三角形面积
def area(d, high):
    return d * high / 2


d = 4
high = 6
print("area=", int(area(d, high)))  # int()返回整数

# 数列集合
a, b = 10, 11
while b > 3:
    print(b)
    a, b = b - a, a

    # 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
    # Fibonacci series: 斐波纳契数列
    # 两个元素的总和确定了下一个数
e, f = 0, 1
while f <100:
    print(f, end=',')
    e, f = f, e + f

