#!/bin/python3
# creating, asigning, typecasting my first value
num1 = int(input("enter a number\n"))
#creating, asigning, typecasting my opreator
opreator = input('enter an opreator eg "+", "-", "*"or "/"\n')
#creating asigning, typecating my second value
num2 = int(input("enter anotther number\n"))
#checking for posibble value of opeator
if opreator == "*":
    result = num1 * num2
elif opreator == "+":
    result = num1 + num2
elif opreator == "-":
    result = num1 - num2
elif opreator == "/":
    result = num1 / num2
else: 
    print('dosn\'t match try "+", "-", "*"or "/"\n')
#    printing thethe vaue of result
str(result)
print("you answer is" + result)
