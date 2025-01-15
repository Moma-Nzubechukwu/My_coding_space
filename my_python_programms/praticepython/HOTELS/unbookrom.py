



def kash(fan):
    file = open('ROOM'+fan+"/status", "r")
    gam = file.readlines()
    if gam[0] == 'OCCUPIED' or gam[0] == "OCCUPIED\n":
        name = input("occupied would you like to un book this room\n")
        if name == "yes":
            paswd = input('enter password\n')
            sam = paswd+'\n'
            gate = open('ROOM'+fan+"/password", "r")
            tame = gate.readlines()
        else:
            return 'no'
            if paswd == tame[0] or sam == tame[0]:
                hight = open('ROOM'+fan+"/status", "w")
                gas = hight.write("NOT OCCUPIED")
                print("done")
            else:
                print("pasword dose notatch")
                return 'no match'
    else:
        print('not occupied')
       return  "not occupied"
