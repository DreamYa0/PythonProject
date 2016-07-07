"""
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda [arg1 [,arg2,.....argn]]:expression
"""
S = lambda arg1, arg2, arg3: arg1 * arg2 + arg3
# 调用函数
print(S(2, 3, 4))
print(S(7, 8, 9))


# return语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
def sum(a, b):
    c = a + b
    print(c)
    return c;


# 调用sum函数
c = sum(2, 3)
c = sum(5, 6)


# 关于return
def cmp(x, y):
    if x < y:
        return -1
    if x == y:
        return 0
    return 1


f = cmp(6, 6)
print(f)
