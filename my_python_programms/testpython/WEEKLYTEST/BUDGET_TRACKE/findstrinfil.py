"""
Starting budget : 2000
Date : 34
Purchases :
Total price : 0
end budget : 2000

"""
def findshit(word, nameOfFiles):

    filobj = open(nameOfFiles, 'r')
    filline = filobj.readlines()
#    print(filline)
    for i in range(len(filline)):
        if word in filline[i].split() and "budget" in filline[i].split():
            ran = (filline[i].split()).index(word)
            

