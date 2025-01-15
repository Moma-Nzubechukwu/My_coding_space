



def caculate_grade(score):
    score = int(score)
    grade = ''
    if score in range(0, 40):
        grade = "F"
    elif score in range(40, 46):
        grade = "E"
    elif score in range(46, 50):
        rade = 'D'
    elif score in range(50, 60):
        grade = "C"
    elif score in range(60, 70):
        grade = "B"
    elif score in range(70, 101):
        grade = "A"
#    else:
#       grade = None"""
    return grade
#your_score = int(input("enter your score"))
#game = caculate_grade(your_score)
#print (game)


