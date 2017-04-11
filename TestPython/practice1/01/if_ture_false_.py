# 猜数字游戏
game = 2
number = 8
while game != number:
    game = int(input('请输入您的数字'))

    if game == number:
        print('恭喜您答对了！')
    elif game > number:
        print('您输入的数字大了')
    elif game < number:
        print('您输入的数字小了')

# if 嵌套
number1 = int(input('请输入一个数字'))
if number1 >50:
    if number1 %2 ==0:
        print('您输入的是一个大于50且能整除2的数')
    else:
        print('您输入的是一个大于50的数')
else:
    if number1 %3 ==0:
        print('您输入的是一个小于50且整除3的数')
    else:
        print('您输入的是一个小于50的数')