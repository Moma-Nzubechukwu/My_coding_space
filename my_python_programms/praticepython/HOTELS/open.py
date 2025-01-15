from random import randint
# this is a file that coppies the content of a file called Room_info and copies it into 36 diffrent files named Room_info in folders named Room{1..36}
for i in range(1, 36):
    room = "ROOM"+str(i)+'/status'
    kall = randint(1,2)
    if kall == 1:
        fow = open(room, 'w')
        fow.write("OCCUPIED")
    if kall == 2:
        fow = open(room, 'w')
        fow.write("NON OCCUPIED")
