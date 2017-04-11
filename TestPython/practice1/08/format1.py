# 字符串格式化
print('大家好，%s叫漫漫，今年读%s,' % ('我', '大班'))
# capitalize()将字符串的第一个字母变成大写,其他字母变小写
aa = 'hi,boy!'
print('capitalize:', aa.capitalize())
# center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
# str.center(width[, fillchar])
s = 'hello,boy!'
print(s.center(20, '2'))

'''
count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

str.count(sub, start= 0,end=len(string))

sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
'''
a = 'this is bad day!'
print('today is:', a.count('s',0,4))
sub = 'is'
print('today ', a.count(sub))

