from collections import deque

'''
P6
对文本做简单的匹配操作，当发现有匹配时就输出当前的匹配行以及最后检查过的N行文本
可以用于在一个文件中查找想要的结果
'''


def search(lines, pattern, history=5):
    # deque(maxlen=N)创建一个固定长度的队列，当有新记录加入而队列长度已满时自动去除最老的那条记录
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('D:\\NewWork\\accountpassword.txt') as f:
        for line, prevlines in search(f, 'huoxianghu@uestc.edu.cn', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('_' * 20)
            prevlines.pop()
