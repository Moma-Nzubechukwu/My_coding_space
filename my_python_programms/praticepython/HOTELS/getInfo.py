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
