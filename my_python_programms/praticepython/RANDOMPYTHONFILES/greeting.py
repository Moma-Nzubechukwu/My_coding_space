#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
print(str)
temp = str[-13] + str[-12]
stor = int(temp)
#print(stor)
if stor < 12:
    print("good morning")
elif stor is range(12, 16):
    print("good afternoon")
elif stor > 16:
    print("good evening")
