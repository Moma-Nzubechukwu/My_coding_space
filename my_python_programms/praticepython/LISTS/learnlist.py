from random import randint
#importing random module


#initializing the daus of the week
days = ["Monday", "Teusday", "Wenesday", "Thursday", "Friday", "Satuday", "Sunday"]
#initializig the subjects
subjects = ["MCT 202", 'CVE 221', 'CVE 222', 'ECE 272', "EEE 251", "MATH 206", "MATH 208", "GSP202", "GSP208", "ECE 251", "MEE 212", "MEE 222"]
spam = [1, 2,range(10, 100), 10]
print(type(spam))
print(len(spam))
print(spam)
print(spam[2])
print(subjects)
#for i in range(100):
#    print(subjects[randint(1, 12)])
for no in range(7):
    print(days[no], end=" ")
    print(':', end="")
    for ram in range(5):
#        print(days[no], end=" ")
 #       print(':', end="")
        print(subjects[randint(1, 11)], end=", ")
    print("/n")
        
    
