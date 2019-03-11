import re

# pattern = r'\d+'
# s = '告别2018, 展望2019'

# pattern = r'\w+:\d+'
pattern = r'(\w+):(\d+)'
s = '张:1995,李:1994'

# 直接用re调用
# l = re.findall(pattern, s)
# print(l)

# compile对象调用
regex = re.compile(pattern)
# l = regex.findall(s)
l = regex.findall(s,pos=0,endpos=10)
print(l)

l = re.split(r'\s+', 'Hello   world  nihao  Kitty')
print(l)

s = re.sub(r'\s+','##','hello world   nihao   Kitty', 2)
print(s)

s = re.subn(r'\s+','##','hello world   nihao   Kitty')
print(s)



