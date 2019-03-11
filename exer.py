import re

f = open('test')
data = f.read()

# l = re.findall(r'\b[A-Z]+\w*', data) #单词

pattern = r'-?\d+[./]?\d*%?'
l = re.findall(pattern, data)

print(l)

