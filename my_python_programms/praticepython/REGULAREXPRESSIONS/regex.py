# a regex that cjecks for isbn 
import re

isbn = input("ISBN\n")

myregexe = re.compile(r'\d\d\d-\d\d\d-\d\d\d-\d\d\d-\d')
mo = myregexe.search(isbn)
print(mo.group())
print(mo)
name = str(mo)
print(name[:9])
