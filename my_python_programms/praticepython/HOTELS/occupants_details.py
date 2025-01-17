


has = input("room no")
name =input("enter occupants name")
phoneno = input("enter occupants phone number")
room = "ROOM"+has+"/ocupant_info"
file = open(room, 'w+')
gash = 'name :'+name+"\n"
phno = "phone number : "+phoneno+"\n"
task = file.writelines([gash, phno])
file.close()
