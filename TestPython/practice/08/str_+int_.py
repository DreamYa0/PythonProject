# ! /usr/bin/python
# 运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换
a = 2
b = "test"
c = str(a) + b
print(c)
d = "1111"
e = a + int(d)

A = '男'
B = '女'
print(A + B)
# How to print multiply values
print("c is %s,e is %i" % (c, e))


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
