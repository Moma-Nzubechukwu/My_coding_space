import re
# a regex that prints the match object


game = input('enter your phone number')
name = re.compile(r'\d{3,}')
mynum = name.search(game)
#print(mynum.group())
print(mynum)
