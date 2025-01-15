from getInfo import getInfo
from checkrom import check_room_status
from checkavi import check_av
from unbookrom import kash


while True:
    whatYouWant = input("what do you want\n1 to check info \n2 to book a room \n3 to unbook a room\n4 to check available rooms\n")

    if whatYouWant == "1":
        name = input("enter your room number\n")
        print("what do you want to check for in Room", name, '\n')
        tame = input()
        yath = getInfo(name, tame)
        home = str(yath[-1])
        if yath[-1] == "yes\n":
            print("yess this room contains a", yath[0])
        elif home.isdecimal() == True:
            print(f"yes{yath[0]} is a vailable in this room and is {yath[1]} in number")

    elif whatYouWant == "2":
        while True:
            name = input("enter your room number\n")
            name = check_room_status(name)
            if name == "true":
                print('the room has been occupied please choose another room\n')
                continue
            elif name == 'false':
                break
            else:
                print("error")
    elif whatYouWant == '3':
        name = input("enter the room number\n")
        kash(name)
    elif whatYouWant == '4':
        check_av()    
