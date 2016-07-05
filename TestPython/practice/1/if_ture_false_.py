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
