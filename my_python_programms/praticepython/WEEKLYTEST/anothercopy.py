import random

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
print(listOfVal)
