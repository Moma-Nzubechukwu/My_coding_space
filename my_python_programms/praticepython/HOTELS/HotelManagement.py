from dt import that
from getInfo import getInfo
from checkrom import check_room_status
from checkavi import check_av
from unbookrom import kash


while True:
    whatYouWant = input("\n\n\n\twhat do you want\n\t1 to check info \n\t2 to book a room \n\t3 to unbook a room\n\t4 to check available rooms\n\t")

    if whatYouWant == "1":
        name = input("enter your room number\n")
        print("what do you want to check for in Room", name, '\n')
        tame = input()
        yath = getInfo(name, tame)
        if tame == "ALL":
            for s in range(len(yath)):
                home = str(yath[s][-1][0])
                if yath[s][-1] == "yes\n":
                    print("yess this room contains a", yath[s][0])
                elif home.isdecimal() == True:
                        print(f"yes{yath[s][0]} is a vailable in this room and is {yath[s][1]} in number")
        else:
            home = str(yath[-1])
            if yath[-1] == "yes\n":
                print("yess this room contains a", yath[0])
            elif home.isdecimal() == True:
                print(f"yes{yath[0]} is a vailable in this room and is {yath[1]} in number")

    elif whatYouWant == "2":
        while True:
            bash = that()
            for i in range(len(bash)):
                print(f" room {bash[i]},", end = "")
            print("is available")
            name = input("enter your room number\n")
            name = check_room_status(name)
            if name == "true":
                print('the room has been occupied please choose another room\n')
                continue
            elif name == 'yes':
                break
            elif name == "no":
                print("ok try another room")
                continue
            else:
                print("error")
    elif whatYouWant == '3':
        name = input("enter the room number\n")
        kash(name)
    elif whatYouWant == '4':
        check_av()    
