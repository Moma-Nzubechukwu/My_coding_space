


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

print("mon tue wed thu fri sat sun")
g = 1
while g <= 31:
    for t in range(5):
        for y in range(7):
            if y <= int(weekdays) and t == 0:
                continue
            print(str(g).rjust(3), end = " ")
            g += 1
        print('\n')

