import re


phonenumber= re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)|(\+\d\d\d\d\d\d\d\d\d\d\d\d\d)')
mo = phonenumber.search('+2349013245212')
print(mo.group())
