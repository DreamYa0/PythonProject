# coding:utf-8
str = 'bad bad bad'
str = str.encode('GBK', 'strict')
print(str)

word = ['a', 'b', 'c', 'd', 'e']
A = word[0:2]
print(A)
B = word[:3]
print('word[:3]:', B)
C = word[0:2] + word[1:5]
print('c is:', C)
print(C)