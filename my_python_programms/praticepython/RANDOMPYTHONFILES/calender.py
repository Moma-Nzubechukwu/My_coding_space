


import sys
# give a date to start and the countimg starts there
weekdays = input("enter the day  1 for mom 2 for teu 3 for wed 4 for thur 5 for fri 6 for sat 7 for 8")
if not weekdays.isdecimal():
    print('not valid')
    sys.exit(0)
if int(weekdays) >= 8:
    print("not valid")
    sys.exit(0)
daysweek = list('Monday Teusday Wensday Thursday Friday Saturday Sunday'.split())
prompt = daysweek[int(weekdays) - 1].lower()
if prompt == 'monday':
    daynum = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,  6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
if prompt == 'tuesday':
    daynum = [31, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
if prompt == 'wensday':
    daynum = [30, 31, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12, 13, 14, 15, 16]
if prompt == 'thursday':
    daynum = [29, 30, 31, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
if prompt == 'friday':
    daynum = [28, 29, 30, 31, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
if prompt == 'saturday':
    daynum = [27, 28, 29, 30, 31, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
if prompt == 'sunday':
    daynum = [26, 27, 28, 29, 30, 31, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
caldic = {'Monday' : [daym1, daym2, daym4, daym5], 
        'Teusday' : [dayt1, dayt2, dayt4, dayt5],
        'Wensday' : [dayw1, dayw2, dayw4, dayw5], 
        'Thursday' : [dayth1, dayth2, dayth4, dayth5], 
        'Friday' : [dayf1, dayf2, dayf4, dayf5], 
        'Saturday' : [days1, days2, days4, days5], 
        'Sunday' : [daysun1, daysun2, daysun4, daysun5]}
"""


daym1, daym2, daym3, daym4, daym5, daym6, daym7, dayt1, dayt2, dayt3, dayt4, dayt5, dayt6, dayt7, dayw1, dayw2, dayw3, dayw4, dayw5, dayw6, dayw7, dayth1, dayth2, dayth3, dayth4, dayth5, dayth6, dayth7, dayf1, dayf2, dayf3, dayf4, dayf5, dayf6, dayf7, days1, days2, days3, days4, days5, days6, days7, daysun1, daysun2, daysun3, daysun4, daysun5, daysun6, daysun7 = daynum

days = [daym1, daym2, daym3, daym4, daym5, dayt1, dayt2, dayt3, dayt4, dayt5, dayw1, dayw2, dayw3, dayw4, dayw5, dayth1, dayth2, dayth3, dayth4, dayth5, dayf1, dayf2, dayf3, dayf4, dayf5, days1, days2, days3, days4, days5, daysun1, daysun2, daysun3, daysun4, daysun5]
caldic = {'Monday' : [daym1, daym2, daym3, daym4, daym5, daym6, daym7],
        'Teusday' : [dayt1, dayt2, dayt3,  dayt4, dayt5, dayt6, dayt7],
        'Wensday' : [dayw1, dayw2, dayw3, dayw4, dayw5, dayw6, dayw7],
        'Thursday' : [dayth1, dayth2, dayth3, dayth4, dayth5, dayth6, dayth7],
        'Friday' : [dayf1, dayf2, dayf3, dayf4, dayf5, dayf6, dayf7], 
        'Saturday' : [ days1, days2, days3, days4, days5, days6, days7],
        'Sunday' : [ daysun1, daysun2, daysun3, daysun4, daysun5, daysun6, daysun7]}



"""
mon tue wed thu fri sat sun
  1   2   3   4   5   6   7
  8   9  10  11  12  13  14
 15  16  17  18  19  20  21
 22  23  24  25  26  27  28
 29  30  31
 """
print("mon tue wed thu fri sat sun")
for t in range(len(daysweek)):
    for y in range(len(caldic[daysweek[t]])):
        print(str(caldic[daysweek[t]][y]).rjust(3), end = " ")
    print('\n')
print(daym1)
