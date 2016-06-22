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
    print('{0:1d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))   #d为格式标识符，表示的double数据类型（双精度）
    # 选项 ':' 和格式标识符可以跟着字段名进行更好的格式化。保留到小数点后某位
table={'mike':11,'pink':12,'Taobao':13,'lol':14}
for name,number in table.items():
    print ('{0:10} {1:20d} '.format(name,number,))


#range函数使用方法
range(4)       #range()函数内只有一个参数，则表示会产生从0开始计数的整数列表
range(1,6)     #当传入两个参数时，则将第一个参数做为起始位，第二个参数为结束位
range(0,6,1)   #填入三个参数，第三个参数是步进值（步进值默认为1）
range(-4,4,-1) #range函数的参数和结果也并非一定要是正数或是递增的

#input()函数支持用户输入数字或者表达式,不支持输入字符串.返回的是数字类型的数值.
#raw_input()函数捕获的是用户的原始输入,返回为字符串.如果需要用输入的数字计算,则需要使用int()函数转换一下.

#python数字金字塔
number=input('please enter a number:''')
number = int(number)
def fun(n):
    nstr=''
    for i in range(n):
        nstr += str(n)+ ' '

    return nstr
for n in range(1, (number + 1)):
    s=fun(n)
    print(s.center(number * 2 +  1))

