import function


"""
file_name = input("enter the file name\n")
fileobj = open(file_name, 'r')
filecontent = fileobj.read()
result = function.invert(filecontent)
gash = function.myhash(result)
#pme r unrint(result)
print(gash)
name = function.myunhash(gash)
gate = function.invert(name)
print(gate)
"""
prompt = input('enter what you want 1 to hash\n 2 to unhash')
if prompt == "1":
    whtYouWant = input("enter 1 what format 1 for sentence\n2 for file")
    if whtYouWant == '1':
       strToHash =  input("enter sentence\n")
       hashed = function.myhash(strToHash)
    if whtYouWant == '2':
        file_to_hash = input('enter the file name you whant to hash')
        fileobj = open(file_to_hash, 'r')
        filecontent = fileobj.read()
        hashed = function.myhash(filecontent)
if prompt == '2':
    whtYouWant = input("enter 1 what format 1 for sentence\n2 for file")
    if whtYouWant == '1':
       strToHash =  input("enter sentence\n")
       hashed = function.myunhash(strToHash)
    if whtYouWant == '2':
        file_to_hash = input('enter the file name you whant to hash')
        fileobj = open(file_to_hash, 'r')
        filecontent = fileobj.read()
        hashed = function.myunhash(filecontent)
print(hashed)



