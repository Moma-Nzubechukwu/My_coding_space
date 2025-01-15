

import re


def ok(name):
    paswobj = open(name, 'r')
    paswrd = paswobj.read()
    new = re.compile(r'(\w){8,}')
    nash = new.search(paswrd)
    #print('this is cjecks for lenght', nash.group())
    cap = re.compile(r'[A-Z]')
    name = cap.search(paswrd)
    #print('this checkes for capital', name.group)
    bic = re.compile(r'[a-z]')
    you = bic.search(paswrd)
    #print('to check for lowr case', you.group())
    jack = re.compile(r'\d')
    male = jack.search(paswrd)
    #print('tocheck for imt ', male.group)
    if name != None and male != None and you != None and nash != None:
#        print('this is a strong password')
        return True
    else:
#        print('not strong enough')
        return None
#print(paswrd)


