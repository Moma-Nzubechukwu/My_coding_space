"""
Develop a password generator that:
- Allows users to specify password length
- Gives options to include/exclude character types
- Generates secure random passwords
- Provides option to save generated passwords
"""
import re
from functions import *

passlen = int(input("enter the lenght of the pasword\n"))
chose = input("yes if you want to add characher that is not in the alphabet and nimbers enter no if you dont\n")
yesorno = re.compile(r'yes', re.I)
mo = yesorno.search(str(chose))
password = genrandpass(passlen, mo)
print("done")
print(password)
save = input('do you whant to save it\n')
yesorno = re.compile(r'yes', re.I)
mo = yesorno.search(save)
if mo != None:
    username = input("enter user name\n")
    details = ["\nuser name:", username, '\n', "password : ", password, "\n"]
    writeobj = open("paswords.txt", 'a')
    gash = writeobj.writelines(details)
    print ('saved')
    




