# ! /usr/bin/python
# 运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换
a = 2
b = "test"
c = str(a) + b
print(c)
d = "1111"
e = a + int(d)
# How to print multiply values
print("c is %s,e is %i" % (c, e))