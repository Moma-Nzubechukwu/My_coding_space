#!bin/bash/python3

# A function that fimds the area of a rectangle

def area(lenght, breath):
    result = lenght * breath
    return result





while True:
    try:
        breath = float(input("enter breath\n"))
        lenght = float(input("enter lenght\n"))
        print('area is ', area(lenght, breath))
        break
    except ValueError:
        print('enter a number')
        continue
    
