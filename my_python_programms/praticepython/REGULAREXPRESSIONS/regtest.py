import re


prompt = input('enter number')

name = re.compile(r'\d(\d)+')
mo = name.search(prompt)
print(mo.group())
