



subjects = []
i = 0
File_object = open(r"subject","w")

while True:
    sub = input("enter the subject\n")
    if sub == "":
        break
    else:
        subjects.append(sub)
print(subjects)
while i < len(subjects):

    hi = str(subjects[i]) + '\n'
    File_object.write(hi)
    i += 1
File_object.close()
