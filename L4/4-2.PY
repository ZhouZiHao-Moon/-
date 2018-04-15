def func(s):
    s2=s.capitalize()
    return s2
# upper()把所有字符中的小写字母转换成大写字母
# lower()把所有字符中的大写字母转换成小写字母
# capitalize()把第一个字母转化为大写字母，其余小写
# title()把每个单词的第一个字母转化为大写，其余小写

print(list(map(func,['adam', 'LISA', 'barT'])))
