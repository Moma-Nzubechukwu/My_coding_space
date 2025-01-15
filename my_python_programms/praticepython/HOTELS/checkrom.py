
def check_room_status(no):
    room = 'ROOM'+no+"/status"
    file = open(room, 'r')
    gash = file.readlines()
    print(gash[0])
    if gash[0] == 'OCCUPIED' or gash[0] == 'OCCUPIED\n':
        print("occupied")
        return "true"
    else:
        print("Not Occupied would you like to book this one")
        name = input('enter yes or no')
        if name == "yes":
            said = open(room, 'w')
            hi = said.write("OCCUPIED")
            print('you have successfully booked this room')
            return 'false'
