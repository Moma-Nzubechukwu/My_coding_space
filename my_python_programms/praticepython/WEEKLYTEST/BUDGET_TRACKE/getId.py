"""
Starting budget : 2000
Date : 34
Purchases :
Total price : 0
end budget : 2000

"""
def getId(catOfid):

    filobj = open('buget.txt', 'r')
    filline = filobj.readlines()
    for i in range(len(filline)):
        if catOfid in filline[i].split():
            splited = (filline[i].split())
            ran = splited.index('id')
            catId = splited[ran + 1]
    return catId




def getItemById(idcat):
    listOfMatchedId = []
    forid = open("buget.txt", 'r')
    idfilline = forid.readlines()
    for i in range(len(idfilline)):
        man = idfilline[i].split()
        if '\n' not in man and man != []:
            comp = man.index('id')
            if idcat == man[comp +1]:
                listOfMatchedId.append(idfilline[i])
    return listOfMatchedId







print(getItemById(input('enter')))
print(getId(input()))
