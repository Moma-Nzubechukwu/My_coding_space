#!/bin/python3
h = 0
g = 0
c = 0
name= ""
b = 1

sentence= input("enter a sentence ")
for h in sentence:
    c = c + 1
   
for I in range(c):
       #for b in range(65, 90):
    if sentence[I-1] == " " or I == 0:
        gash = (ord(sentence[I]))
        had = gash - 32
        print(chr(had), end ="")
    else :
        print(sentence[I], end = "") 
#print(name)             
                
