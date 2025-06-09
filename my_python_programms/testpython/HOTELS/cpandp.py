# this is a file that coppies the content of a file called Room_info and copies it into 36 diffrent files named Room_info in folders named Room{1..36}
for i in range(1, 36):
    
    room = 'ROOM'+str(i)+"/password"
    fow = open(room, 'w')
    fow.write(room)
