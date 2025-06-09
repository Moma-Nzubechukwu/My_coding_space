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
