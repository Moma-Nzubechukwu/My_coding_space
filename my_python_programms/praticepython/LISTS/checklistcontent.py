




name = input("enter your name\n")
age = int(input("enter your age\n"))
nikName = input("enter your nickname\n")
person = [name, age, nikName]
names = ['moma', 'nzube', 'fransisco', 'pablo', 'robert']
nickname = ["shadow", "a.gold", "death"]
ages = [18, 19, 20, 21, 22, 23, 24, 25]
if name in names:
    if nikName in nickname:
        if age in ages:
            print("accsess granted")
        else:
            print("acsess denied")
    else:
        print("acsess denied")
else:
    print("acsess denied")





