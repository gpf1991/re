import re

pattern = r'\d+'
s = '告别2018, 展望2019'

regex = re.compile(pattern)

# l = regex.findall(s)
l = regex.findall(s, pos=0,endpos=31)
print(l)

regex = re.compile(r'\s+')
l = regex.split('hello zyy hello,China World   Kitty')
print(l)

s1 = regex.sub('**','hello zyy hello  China World   Kitty')
print(s1)

s2 = regex.subn('@', 'hello zyy hello  China World   Kitty')
print(s2)

s3 = '2018年中国经济增长6.6%,与2017年基本持平，\
2019面临很多困难'
# regex = re.compile(r'\d+')
# it = regex.finditer(s3)
# # print(dir(next(it)))
# for i in it:
#     print(i.group())

regex = re.compile(r'\w+')
try:
    obj = regex.fullmatch('hellozyy')
    print(obj.group())
except AttributeError as e:
    print(e)

regex = re.compile(r'[A-Z]\w+')
try:
    obj = regex.match('Hello Zyy')
    print(obj.group())
except AttributeError as e:
    print(e)

regex = re.compile(r'\d+')
try:
    obj = regex.search(s3)
    print(obj.group())
except AttributeError as e:
    print(e)

