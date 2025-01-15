
File_object = open(r"File_Name","w")

name = input("enter your name:\n")
age = input("enter your age: \n")
shadow = {"name": name, 'age':age}
print(shadow)
value = shadow.values()
print("these are the value entered", value)


hi = list(shadow.values())
for i in range(len(hi)):
    File_object.write(hi[i])
    File_object.write('\n')

File_object.close()
