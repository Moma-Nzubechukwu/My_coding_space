
from pprint import pprint
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


enterdmonth = "02"

'''
#if enterdmonth in list(montOfYear.values()) + list(montOfYear.keys()):
    print('ok')
if enterdmonth not in list(montOfYear.items()):
    print("hi")
print(list(montOfYear.items()), len(list(montOfYear.items())))
pprint(list(montOfYear.items()))
'''
pprint(list(montOfYear.values()))
