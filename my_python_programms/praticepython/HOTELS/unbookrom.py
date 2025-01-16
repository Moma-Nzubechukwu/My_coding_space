



def kash(fan):
    file = open('ROOM'+fan+"/status", "r")
    gam = file.readlines()
    if gam[0] == 'OCCUPIED' or gam[0] == "OCCUPIED\n":
        name = input("occupied would you like to un book this room\n")
        if name == "yes":
            a = 0
            while a < 5:
                paswd = input('enter password (you have only 5 atempts)\n')
                sam = paswd+'\n'
                gate = open('ROOM'+fan+"/password", "r")
                tame = gate.readlines()
                if paswd == tame[0] or sam == tame[0]:
                    hight = open('ROOM'+fan+"/status", "w")
                    gas = hight.write("NOT OCCUPIED")
                    print("done")
                    break
                else:
                    print("pasword dose notatch")
                    a = a + 1
        else:
            return "no"
    else:
        print('not occupied')
        return "not occupied"
