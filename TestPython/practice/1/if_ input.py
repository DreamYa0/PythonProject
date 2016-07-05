# 关于工资的计算
wages = int(input('请输入你的工资'))
print('')
if wages < 0:
    print('你还真是个败家子')
elif wages == 0:
    print('你是月光族')
elif wages <= 4000:
    print('你的工资低于平均水平')
elif wages > 4000:
    print('你的工资等于平均水平')
elif wages >= 5000:
    print('你的工资高于平均水平')
# 退出
input('点击enter键退出')
