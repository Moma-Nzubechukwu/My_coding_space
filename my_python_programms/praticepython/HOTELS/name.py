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
