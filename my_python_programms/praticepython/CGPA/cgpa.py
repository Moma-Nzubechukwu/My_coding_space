



def caculate_cgpa(unitLoad, score, totalUnitLoad):
    result = unitLoad * score
    cgpa = result / totalUnitLoad
    return cgpa




name = 0
listOfScores = []
listOfLoad = []
listOfSubject = []
course = int(input("enter how many course you want to check"))
totalUnitLoad = int(input("enter the total unit load you offer\n"))
for i in range(course):
    subject = input("enter the subject name\n")
    load = int(input('enter you unit load for ' + subject + '\n'))
    yourScore = int(input('enter your score for '+ subject + '\n'))
    listOfScores.append(yourScore)
    listOfLoad.append(load)
    listOfSubject.append(subject)
for b in range(course):
    name += caculate_cgpa(listOfLoad[b], listOfScores[b], totalUnitLoad)
    
print("your cgpa is", name)



