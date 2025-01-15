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
