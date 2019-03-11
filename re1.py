import re

pattern = r'\d+'
s = '2018年中国经济增长6.6%,与2017年基本持平，\
2019面临很多困难'

it = re.finditer(pattern, s)

# match对象属性
# print(dir(next(it)))

# match对象属性
# 'end', 'endpos', 'expand', 'group', \
# 'groupdict', 'groups', 'lastgroup', \
# 'lastindex', 'pos', 're', 'regs', \
# 'span', 'start', 'string'


# for i in it:
#     # print(i)
#     print(i.group())

try:
    # obj = re.fullmatch(r'\w+','hello#1973')
    obj = re.fullmatch(r'\w+','hello1973')
    print(obj.group())
except AttributeError as e:
    print(e)

try:
    # obj = re.match(r'[A-Z]\w+', '## Hello world')
    obj = re.match(r'[A-Z]\w+', 'Hello world')
    print(obj.group())
except AttributeError as e:
    print(e)

try:
    # obj = re.search(r'\d+', '## Hello world')
    obj = re.search(r'\d+', s)
    print(obj.group())
except AttributeError as e:
    print(e)

