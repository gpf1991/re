# 找一个文档，使用正则表达式匹配
#   1）所有以大写字母开头的单词
#   2）所有的数字，包含整数，小数，负数，分数，百分数


import re

capital_letter = []
num_list = []

f = open('./111.txt', 'rt')
while True:
    data = f.read(1024)
    if not data:
        import time
        time.sleep(0.1)
        break
    # word = re.findall(r'[A-Z]+[a-z]*', data)
    # capital_letter += word
    num = re.findall(r'\b-?\d+[./]?\d*%?\b', data)
    num_list += num

f.close() 
# print(capital_letter)

print(num_list)

