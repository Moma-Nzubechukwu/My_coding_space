


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
