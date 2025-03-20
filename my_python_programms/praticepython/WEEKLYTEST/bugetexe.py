"""
Starting budget : 2000
Date : 34
Purchases :
Total price : 0
end budget : 2000
"""
from pprint import pprint

filobj = open("buget.txt", 'r')
filline = filobj.readlines()
pprint(filline)
for i in range(len(filline)):
    if "Starting" in filline[i].split() and "budget" in filline[i].split():
        print(filline[i].split()[-1])

