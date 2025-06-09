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
