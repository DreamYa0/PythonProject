# python输入与输出
# 两种输出值的方式: 表达式语句和 print() 函数。第三种方式是使用文件对象的 write() 方法
# 标准输出文件可以用 sys.stdout 引用。 str.format() 函数来格式化输出值。将输出的值转成字符串，可以使用 repr()(解释器易读) 或 str() (用户易读)函数

a = 25;
b = 10
s = 'a的值为: ' + repr(a) + ' , b的值为:' + repr(b) + ''
print(s)

aa = 'hi\n'  # repr()函数可以转义字符串中的特殊字符
bb = repr(aa)
print(bb)

aa = 'h\ni'
print(aa)  # \n 换行

# format() 函数格式：print('{}{}{}'.format(a,b,c))
print('{}网址：{}'.format('刺鸟','www.ciniao.com'))  #输出字符串
print('{} {}'.format(1,4))                           #输出数值
# 立方表
for x in range(1, 11):
    print('{0:1d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))   #d表示的double数据类型（双精度）


