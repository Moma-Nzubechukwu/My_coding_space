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
                continue
            else:
                print("error")
    elif whatYouWant == '3':
        name = input("enter the room number\n")
        kash(name)
    elif whatYouWant == '4':
        check_av()    
    elif whatYouWant == '5':
        break
from jassent import spaceList
from get import check_for_hotel

def bat(hi, contentOfRoom):
    info = ["window", "door", "balcony", "bed", "socket", "floor", "fan", "bulb", "chair"]
    fin =[]
    for h in range(len(contentOfRoom)):
        for g in range(len(info)):
            if info[g] in spaceList(contentOfRoom[h]):
                jack = spaceList(contentOfRoom[h])
                gat = jack.index(info[g])
#                print(gat)
                fin.append([jack[gat], jack[-1]])


    return fin
from jassent import spaceList


def book(contentOfRoom, whatYouWantToCheck):
    for i in range(len(contentOfRoom)):
        for t in range(len(contentOfRoom[i])):
            if contentOfRoom[i][t] == 'whatYouWantToCheck':
                print('your rooms',contentOfRoom[i][:t-1], 'is',  contentOfRoom[i][t+1:])



def check_av():
    rooms = []
    for name in range(1, 36):
        name = str(name)
        yath =open("ROOM"+name+"/status", 'r')
        tame = yath.readlines()
        if tame[0] == 'OCCUPIED' or tame[0] == "OCCUPIED\n":
                print(f"room {name} is occupied")
        else:
            print(f"room{name} is not occupied")
from occupants_details import occupantInfo
def check_room_status(no):
    room = 'ROOM'+no+"/status"
    file = open(room, 'r')
    gash = file.readlines()
    if gash[0] == 'OCCUPIED' or gash[0] == 'OCCUPIED\n':
        print("occupied")
        return "true"
    else:
        print("Not Occupied would you like to book this one")
        name = input('enter yes or no')
        if name == "yes":
            said = open(room, 'w')
            name = input("Enter name\n")
            phoneno = input("Enter yoir phome number")
            occupantInfo(no, name, phoneno)
            hi = said.write("OCCUPIED")

            print('you have successfully booked this room')
            return 'yes'
        elif name == "no":
            return 'no'
# this is a file that coppies the content of a file called Room_info and copies it into 36 diffrent files named Room_info in folders named Room{1..36}
for i in range(1, 36):
    
    room = 'ROOM'+str(i)+"/password"
    fow = open(room, 'w')
    fow.write(room)



def that():
    rooms = []
    for name in range(1, 36):
        name = str(name)
        yath =open("ROOM"+name+"/status", 'r')
        tame = yath.readlines()
        if tame[0] == 'OCCUPIED' or tame[0] == "OCCUPIED\n":
            hi = name
        else:
            rooms.append(name)
   # print(rooms)
    return rooms
from jassent import spaceList


roomNumber = input("enter a room number")
yourRoomNumber = 'ROOM'+roomNumber+"/Room_info"
romobj = open(yourRoomNumber, 'r')
contentOfRoom = romobj.readlines()
#print(len(contentOfRoom))
print(contentOfRoom)
for i in range(len(contentOfRoom)):
    for t in range(len(contentOfRoom[i])):
        if contentOfRoom[i][t] == ':':
#            if contentOfRoom[i][t] =
            print('your rooms',contentOfRoom[i][:t-1], 'is',  contentOfRoom[i][t+1:])
#    print(contentOfRoom[i][1])
#print(spaceList(contentOfRoom))
#print(len(spaceList(contentOfRoom)))
from jassent import spaceList


def check_for_hotel(hi, contentOfRoom):
    fin = []
    for h in range(len(contentOfRoom)):
        if hi in spaceList(contentOfRoom[h]):
            hello = spaceList(contentOfRoom[h])
            if hello[-1][0].isdecimal():
                hello[-1] = int(hello[-1])
                if hello[-1] > 0:
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]
                elif hello[-1] <= 0:
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]
            else:
                if hello[-1][:-1] == 'yes':
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]
                elif hello[-1][:-1] == 'none':
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]


    return fin
from jassent import spaceList
from get import check_for_hotel
from bat import bat




def getInfo(roomNumber, hi):

    while True:
        info = ["window", "door", "balcony", "bed", "socket", "floor", "fan", "bulb", "chair"]
        fin = []
#        roomNumber = input("enter a room number\n")
        if roomNumber != "ALL":
            number = int(roomNumber)
            if number > 36:
                continue
        yourRoomNumber = 'ROOM'+roomNumber+"/Room_info"
        romobj = open(yourRoomNumber, 'r')
        contentOfRoom = romobj.readlines()
        fin = check_for_hotel(hi, contentOfRoom)
        if hi == "ALL":
            fin = bat(hi, contentOfRoom)

        break
    return fin
from jassent import spaceList
def getInfo(roomNumber):

    while True:
    
        roomNumber = input("enter a room number\n")
        number = int(roomNumber)
        if number > 36:
            continue
        number = str(roomNumber)
        yourRoomNumber = 'ROOM'+roomNumber+"/Room_info"
        romobj = open(yourRoomNumber, 'r')
        contentOfRoom = romobj.readlines()
        print("what do you want to check for in Room", roomNumber, '\n')
        hi = input()
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


#this is a code that sepreats each word of a sentence  and stores it in a list data type

def spaceList(prompt):
    name = ''
    post = []
    for i in range(len(prompt)):
        if prompt[i] != ' ':
            name += prompt[i]
        else:
            post.append(name)
            name = ''
            continue
    post.append(name)
    #print(post)
    return post
from jassent import spaceList


roomNumber = input("enter a room number")
yourRoomNumber = 'Room'+roomNumber
romobj = open(yourRoomNumber, 'r')
contentOfRoom = romobj.readlines()
#print(len(contentOfRoom))
print(contentOfRoom)
for i in range(len(contentOfRoom)):
    for t in range(len(contentOfRoom[i])):

        if contentOfRoom[i][t] == ':':
#            if contentOfRoom[i][t] =
            print('your rooms',contentOfRoom[i][:t-1], 'is',  contentOfRoom[i][t+1:])
#    print(contentOfRoom[i][1])
#print(spaceList(contentOfRoom))
#print(len(spaceList(contentOfRoom)))
from jassent import spaceList
roomNumber = input("enter a room number\n")
#number = int(roomNumber)
#if number > 36:
#    continue
#number = str(roomNumber)
yourRoomNumber = 'Room_info'#'ROOM'+roomNumber+"/Room_info"
romobj = open(yourRoomNumber, 'r')
contentOfRoom = romobj.readlines()
print(len(contentOfRoom))
print(contentOfRoom)
print(yourRoomNumber)




def occupantInfo(rom_no, ocpt_name, ocpt_phoneno):
    room = "ROOM"+rom_no+"/ocupant_info"
    file = open(room, 'w+')
    gash = 'name : '+ocpt_name+"\n"
    phno = "phone number : "+ocpt_phoneno+"\n"
    task = file.writelines([gash, phno])
    file.close()
from random import randint
# this is a file that coppies the content of a file called Room_info and copies it into 36 diffrent files named Room_info in folders named Room{1..36}
for i in range(1, 36):
    room = "ROOM"+str(i)+'/status'
    kall = randint(1,2)
    if kall == 1:
        fow = open(room, 'w')
        fow.write("OCCUPIED")
    if kall == 2:
        fow = open(room, 'w')
        fow.write("NON OCCUPIED")

from getInfo import getInfo


hi = input('enter')
hi = getInfo(hi)
print(hi)




def kash(fan):
    file = open('ROOM'+fan+"/status", "r")
    gam = file.readlines()
    if gam[0] == 'OCCUPIED' or gam[0] == "OCCUPIED\n":
        name = input("occupied would you like to un book this room\n")
        if name == "yes":
            a = 0
            while a < 5:
                paswd = input('enter password (you have only '+ str(5 - a) + ' atempts)\n')
                sam = paswd+'\n'
                gate = open('ROOM'+fan+"/password", "r")
                tame = gate.readlines()
                if paswd == tame[0] or sam == tame[0]:
                    hight = open('ROOM'+fan+"/status", "w")
                    gas = hight.write("NOT OCCUPIED")
                    print("done")
                    break
                else:
                    print("pasword dose notatch")
                    a = a + 1
        else:
            return "no"
    else:
        print('not occupied')
        return "not occupied"
from jassent import spaceList



jas = open("ROOM24/Room_info", 'r')
hi = jas.readlines()
hi = spaceList(hi)
print(hi)


from jassent import spaceList

fin = []
info = ["window", "door", "balcony", "bed", "socket", "floor", "fan", "bulb", "chair"]
#        roomNumber = input("enter a room number\n")                                            if roomNumber != "ALL":
yourRoomNumber = "ROOM24/Room_info"
romobj = open(yourRoomNumber, 'r')
contentOfRoom = romobj.readlines()
for h in range(len(contentOfRoom)):
    for g in range(len(info)):
        if info[g] in spaceList(contentOfRoom[h]):
            jack = spaceList(contentOfRoom[h])
            gat = jack.index(info[g])
#                            print(gat)
            fin.append([jack[gat], jack[-1]])
print(fin)
