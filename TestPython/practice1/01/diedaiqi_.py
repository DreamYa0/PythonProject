# 迭代器有两个基本的方法：iter() 和 next()

import sys                            # 导入sys模块

List = [0, 1, 2, 3, 4]
L = iter(List)  # 创建一个迭代对象
for x in L:
    print(x,end='')

# next()函数

list1 = [1, 2, 3, 4]
it = iter(list1)

while True:                            # 当为真时，即死循环时
    try:                               # 试着打印它
        print(next(it))
    except StopIteration:              # 除上面的之外就停止迭代
        sys.exit()                     # 跳出系统