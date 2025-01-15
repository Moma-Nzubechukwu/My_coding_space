import re

isbn = input("isbn")

myregexe = re.compile(r'\d\d\d-\d\d\d-\d\d\d-\d\d\d-\d')
mo = myregexe.search(isbn)
print(mo.group())
print(mo)
name = str(mo)
print(name[:9])
