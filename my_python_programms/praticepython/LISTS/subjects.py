from random import randint
#importing random module


#initializing the daus of the week
days = ["Monday", "Teusday", "Wenesday", "Thursday", "Friday", "Satuday", "Sunday"]
#initializig the subjects
subjects = ["MCT 202", 'CVE 221', 'CVE 222', 'ECE 272', "EEE 251", "MATH 206", "MATH 208", "GSP202", "GSP208", "ECE 251", "MEE 212", "MEE 222"]
#creating aloop that will loop through the days of the week
for no in range(7):
    print(days[no], end=" ")
    print(':', end=" ")
    #creating a loop that will loop through and print the subjecys
    for ram in range(5):
        print(subjects[randint(1, 11)], end="")
        print(',', end = "")
    print('\n')

        
    