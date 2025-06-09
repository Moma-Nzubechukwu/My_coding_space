from get import check_for_hotel
from jassent import spaceList

"""
if status is vacant amd print rooms that are vacant
"""

#def book_a_room():
 #   if status == vacant
name = open("ROOM24/Room_info", "r")
hello = name.readlines() 
#print(check_for_hotel("floor", hello))
hi = "status"
#dash = spaceList(hello)
#print (dash[-1][:-1])
for i in range(len(hello)):
    if hi in spaceList(hello[i]):
        dash = spaceList(hello)
        print(spaceList(hello[i])[-1])
        if spaceList(hello[i])[-1] == 'Occupied\n':
            print(hi)
