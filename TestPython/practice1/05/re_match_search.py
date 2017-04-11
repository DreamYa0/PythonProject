import re

# match()函数只检测RE是不是在string的开始位置匹配 search()会扫描整个string查找匹配,会扫描整个字符串并返回第一个成功的匹配
print(re.match('hello', 'hello,what is your name?').span())
print(re.search('is', 'hello,what is your name?').span())

line = 'hello,what is your mother name?'
matchObj = re.match(r'(.*) is (.*?) .*', line, re.M)
if matchObj:
    print('matchObj.group():', matchObj.group())
    print('matchObj.group():', matchObj.group(1))
    print('matchObj.group():', matchObj.group(2))
else:
    print('no match!')

line2 = 'what is your mother name?'
searchObj = re.search(r'(.*) your (.*?) .*', line2, re.I)
if searchObj:
    print('searchObj.group():', searchObj.group())
    print('searchObj.group():', searchObj.group(1))
    print('searchObj.group():', searchObj.group(2))
else:
    print('find out!')
