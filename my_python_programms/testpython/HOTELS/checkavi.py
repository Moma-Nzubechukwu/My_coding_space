


def check_av():
    rooms = []
    for name in range(1, 36):
        name = str(name)
        yath =open("ROOM"+name+"/status", 'r')
        tame = yath.readlines()
        if tame[0] == 'OCCUPIED' or tame[0] == "OCCUPIED\n":
                print(f"room {name} is occupied")
        else:
            print(f"room{name} is not occupied")
