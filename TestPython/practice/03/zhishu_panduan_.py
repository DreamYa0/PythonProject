# 质数判断
number = int(input('请输入一个数字：'))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print('输入的不是质数')
            print(i, '*', number // i, '=', number)
            break
    else:
        print('输入的是质数')
else:
    print('输入的不是质数')
