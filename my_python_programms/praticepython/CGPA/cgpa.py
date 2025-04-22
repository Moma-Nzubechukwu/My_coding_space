"""
*listOfScores - an empty list that is to store a list of scores entered by the user
*listOfLoad - an empty list that is to store a list of unit load entered by the user
*listOfSubject - an empty list that is to store a list of subject entered by the user
*course - a variable used to store the user input when asked  "how many course you wants to check"
*subject - stores the user input when asked "enter subject name" stores the name of the subject that is been caculated and is appended to listOfSubject 
*load - stores theusers inpit when asked "enter unit load" is to store the unit load of the subject being caculated and is appended to the listOfLoad list
*yourScore - stores the input when aksed "enter your score" is to store the the score on the subject

"""



def caculate_cgpa(unitLoad, score, totalUnitLoad):
    """
    a function that caculate the gpa for a single course
    
    """
    result = unitLoad * score
    cgpa = result / totalUnitLoad
    return cgpa




name = 0
listOfScores = []
listOfLoad = []
listOfSubject = []
course = int(input("enter how many course you want to check\n"))
totalUnitLoad = int(input("enter the total unit load you offer\n"))
for i in range(course):
    subject = input("enter the subject name\n")
    load = int(input('enter you unit load for ' + subject + '\n'))
    yourScore = int(input('enter your score for '+ subject + '\n'))
    #appends the values to its corresponding list
    listOfScores.append(yourScore)
    listOfLoad.append(load)
    listOfSubject.append(subject)
for b in range(course):
    # a for loop that calculates the cgpa by call ing the function caculaye_cgpa amd summing up the returned value
    name += caculate_cgpa(listOfLoad[b], listOfScores[b], totalUnitLoad)
#printing the cgpa
print("your cgpa is", name)



