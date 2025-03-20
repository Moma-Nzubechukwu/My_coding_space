import random

thingBought = ""
totalPrice= 0
flist = []
montOfYear = {'01': ["JANUARY", "JAN"],
        '02' : ["FEBUARY", "FEB"],
        '03' : ["MARCH", 'MAR'],
        '04' : ['APRIL', 'APR'],
        '05' : ['MAY'],
        '06' : ['JUNE', 'JUN'],
        '07' : ['JULY', "JUL"],
        '08' : ["AUGUST", 'AUG'],
        '09' : ["SEPTEMBER", "SEP"],
        '10' : ["OCTOBER", "OCT"],
        '11' : ["NOVEMBER", "NOV"],
        '12' : ["DECEMBER", 'DEC']}



lisval = list(montOfYear.values())
listOfVal = []
for i in range(len(lisval)):
    for j in range(len(lisval[i])):
        listOfVal.append(lisval[i][j])
monthkv = listOfVal + list(montOfYear.keys())    
daysenterd = int(input('enter the ammount of days you whant to save\n'))
for day in range(daysenterd):
    DAY = input("enter the date\n")
    while True:
        enterdmonth = input("enter the month\n")
#        print(monthkv)
        if enterdmonth.upper() not in monthkv:
            print('not a valid month')
            continue
        elif enterdmonth.isdecimal():
            month = enterdmonth
            break        
        elif enterdmonth.isdecimal():
            monthno  = montOfYear.value().index(enterdmomth)
            month = montOfYear.keys(monthno)
            break
        elif enterdmonth.upper() in listOfVal:
            for a in range(len(lisval)):
                for r in range(len(lisval[a])):
                    if enterdmonth.upper() in lisval[a]:
                        print("hi")
                        month = list(montOfYear.keys())[a]
            break






    year = input("enter  year\n")
    today = DAY + "-" + month + "-" + year
    startingB = int(input("enter starting budget should be only numbers else it will throw an error\n"))
    while True:
        whatYouBought = input("enter what you bought\n")
        if whatYouBought == "":
            break
        price = int(input("enter price of what you bought in naira must be integer click enyer or return to exit to the next day \n"))
        if whatYouBought == "":
            break
        elif str(price).isdecimal():
            thingBought += ", " + whatYouBought
            totalPrice += price
    dayid = (random.randint(1, 10000) * int(DAY))
    sbuget = "Starting budget : ( " + "id "+ str(dayid) + " ) " + str(startingB) + "\n"
    date = "Date : " + "( id "+ str(dayid) + " ) "+ today + "\n"
    bought = "Purchases : " + "(  id "+ str(dayid) + " ) "+ thingBought + "\n"
    tprice = "Total price : " + " ( id "+ str(dayid) + " ) "+ str(totalPrice) + "\n"
    endbuget = "end budget : "+ " ( id "+ str(dayid) + " ) " + str(startingB - totalPrice) + "\n\n\n\n"
#    if month ==







    bugetList = [sbuget, date, bought, tprice, endbuget]
    fobj = open("buget.txt", 'a')
    fobj.writelines(bugetList)
    whatYouBought = ""
    totalPrice = 0
    thingBought = ""
    totaPrice = 0



