from pasw import ok


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
        file.close()
    elif gas != '':
        print("you already have a password")
        break
    if ok("password.txt") == True:
        print("paswod strong")
        break
    else:
        print("passwod not strong")
        break
#    else:
 #       print("pasword saved")
  #      break
#    file.close()
    fileobj.close()
#print(ok("password.txt"))

