import cmath
# 3.0版本已经没有raw_input
num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

a = 3
b = 5
c = a ** 3 + b
print(c)
