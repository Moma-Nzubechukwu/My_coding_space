"""
**Project Description:**
Create a simple budget tracking application that allows users to:
- Add income
- Record expenses in different categories
- Calculate total spending
- Generate a simple monthly summary
- Save and load budget data from a fie

Starting budget : 2000
Date : 34
Purchases :
Total price : 0
end budget : 2000
"""
# this file is ment to to go into buget.txt lookfor the startimg buget and return its id





from pprint import pprint

filobj = open("buget.txt", 'r')
filline = filobj.readlines()
#pprint(filline)
#longlist = filline[i].split()
for i in range(len(filline)):
    longlist = filline[i].split()
    if "Starting" in filline[i].split() and "budget" in filline[i].split():
        sbsprice = filline[i].split()[-1]
        if 'id' in filline[i].split():
            sbsidindex = filline[i].split().index('id') + 1
            sbsid  = longlist[sbsidindex]
            print(sbsid)




