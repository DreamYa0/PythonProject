"""
数据类型转换
int(x)   将X转换为整数
str(x)   将x转换为字符串
repr(x)  将对象X转换为表达式字符串
tuple(s)将序列s转换为一个元组
list(s)  将序列s转换为一个列表
set(s)   转变为可变集合
dict(d)  创建一个字典，d 必须是一个序列 (key,value)元组
chr(x)   将一个整数转换为一个字符
unichr(x)将一个整数转换为Unicode字符
ord(x)   将一个字符转换为它的整数值
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
"""

'''
算术运算符
/ 除
% 取模-余数
**幂-返回x的y次幂
//取整除 - 返回商的整数部分
'''
a = 14
b = 10
c1 = a - b
print('a-b:', c1)
c2 = a + b
print('a+b:', c2)
c3 = a / b
print('a/b:', c3)
c4 = a % b
print('a%b:', c4)
c5 = a ** b
print('a**b:', c5)
c6 = a // b
print('a//b:', c6)

'''
赋值运算符
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''
'''
逻辑运算符
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 True，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''
a = 10
b = 20
if a and b:
    print('变量为true')
else:
    print('变量有一个为false')
if a or b:
    print('变量都为true，或者其中有一个为true')
else:
    print('变量都为false')
if not (a and b):
    print('其中一个变量为false或者全部为false')
else:
    print('变量都为true')

'''
身份运算符
is	is是判断两个标识符是不是引用自一个对象	x is y, 如果 id(x) 等于 id(y) , is 返回结果 01
is not	is not是判断两个标识符是不是引用自不同对象	x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 01
'''
a = 10
b = 5
if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print('4 - a 和 b 有相同的标识')

    # 在交互模式中，最后被输出的表达式结果被赋值给变量 _, _ 变量应被用户视为只读变量

    #   pi	数学常量 pi（圆周率，一般以π来表示）,   e	数学常量 e，e即自然常数（自然常数）。

# 访问字符串中的值
var1 = 'hi,boy!'
var2 = 'python'
print('啊:', var1[0:3])
print('re:', var2[3:5])

# 更新字符串
var = 'python'
print('更新的字符串为：', 'hi  ' + var)

'''
续行符 (黄色第一列\为转义标识符仅此记录用)
\(在行尾时)	续行符
\\\	反斜杠符号
\\'	单引号
\\"	双引号
\\a	响铃
\\b	退格(Backspace)
\e	转义
\\000	空
\\n	换行
\\v	纵向制表符
\\t	横向制表符
\\r	回车
\\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出
'''