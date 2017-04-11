# 1到100求和
n = 1
sum = 0
while n < 101:
    sum = sum + n
    n +=1
print(sum)

# 01~100偶数之和
n1 = 1
sum1 = 0
while n1 <101:
    if n1 %2==0:
        sum1 +=n1
    n1 += 1
print(sum1)