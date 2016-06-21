#!/usr/bin/python3
import sys;x = 'roob';sys.stdout.write(x + '\n')


#标准数据类型
#Number（数字）String（字符串）List（列表）Tuple（元组）Sets（集合）Dictionary（字典）


#列表：加号（+）是列表连接运算符，星号（*）是重复操作

list=[1,2,3,4,]
list1=['a','b']
print(list)
print(list[2])
print(list1 * 2)
print(list + list1)

#列表中的元素是可以改变的

a=[1,2,3,4,5]
a[0]=9
print(a)

#元组

i=('ab','cd','ef')
print (i[0:2])

#i(0)=(5)；print (i)  修改元组的元素是非法的操作

#字符串

te='hello,boy'
print(te[0:2])

#集合（set）是一个无序不重复元素的序列

student={'mm','nn','bb','vv','mm'}
print(student)                    #输出集合，重复的元素被自动去掉
if ('aa' in student) :
      print('aa在集合中')
else:
      print('aa不在集合中')