from jassent import spaceList



jas = open("ROOM24/Room_info", 'r')
hi = jas.readlines()
hi = spaceList(hi)
print(hi)


