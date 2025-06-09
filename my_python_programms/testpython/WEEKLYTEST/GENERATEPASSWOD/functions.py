import random

def genrandpass(passlen, yesorno):
    if yesorno != None:
        #from function import *
        cap = random.randint(0, 15)
        pasword = ''
        for i in range(passlen):

            randnum = random.randint(33, 126)
            inttochar = chr(randnum)
            if i == cap:
                inttochar = chr(randnum).upper()
            pasword += inttochar
    else:
        cap = random.randint(0, 15)
        pasword = ''
        for i in range(passlen):
            while True:
                randnum = random.randint(33, 126)
                if not chr(randnum).isalpha():
                    continue
                else:
                    break
            inttochar = chr(randnum)
            if i == cap:
                 inttochar = chr(randnum).upper()
            pasword += inttochar
    return pasword
