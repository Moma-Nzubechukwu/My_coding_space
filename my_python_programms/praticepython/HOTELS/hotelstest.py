#A file that reads the content of a file and prints some needed part of the file
'''
roomNumber stores the number you emtered
number stores the int version of the number you entered in order for the if statment to work

'''
from jassent import spaceList
#
while True:
    
    roomNumber = input("enter a room number\n")
    number = int(roomNumber)
    if number > 36:
        continue
    #below opens the file
    yourRoomNumber = 'ROOM'+roomNumber+"/Room"+roomNumber
    romobj = open(yourRoomNumber, 'a+')
    contentOfRoom = romobj.readlines()
    print("what do you want to check for in Room", roomNumber, '\n')
    hi = input()
    #down check for some conditions to print something
    for h in range(len(contentOfRoom)):
        if hi in spaceList(contentOfRoom[h]):
            hello = spaceList(contentOfRoom[h])
            if hello[-1][0].isdecimal():
                hello[-1] = int(hello[-1])
                if hello[-1] > 0:
                    print('the item you are looking for is available and is', hello[-1], "in number'\n")
                elif hello[-1] <= 0:
                    print("not available in Room", roomNumber, '\n')
            else:
                if hello[-1][:-1] == 'yes':
                    print(" it is available in Room", roomNumber, '\n')
                elif hello[-1][:-1] == 'none':
                    print("not available in this room", roomNumber, '\n')
    break
