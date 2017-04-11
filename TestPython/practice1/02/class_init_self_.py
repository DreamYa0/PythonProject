# 定义类
class bus:
    seat = 0
    number = 0
    Handrail = 0

    # 定义构造方法
    def __init__(self, s, n, H):
        self.seat = s
        self.number = n
        self.Handrail = H

    def ride(self):
        print("这辆bus上有%d个座位，%d个乘客" % (self.seat, self.number))


# 实例运行
B = bus(30, 40, 10)
B.ride()
