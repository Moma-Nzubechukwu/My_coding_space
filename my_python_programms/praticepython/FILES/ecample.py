#print(paswrd)


while True:
    fileobj = open("password.txt", "r")
    gas = fileobj.read()
#    print(gas)
#if gas == '':
#    print("ok")
    if gas == '':
        pasword = input("enter pasword")
        file = open("password.txt", 'w')
        gash =file.write(pasword +'\n')
    else:
        break
    print(gas)
    file.close()
fileobj.close()
#    print(gas)
