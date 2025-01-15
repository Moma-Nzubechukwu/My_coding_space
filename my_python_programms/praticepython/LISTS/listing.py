#A function that apends something to a list
#the function that apends a word to a list
def appending(value, apend):
    value.append(apend)
    return value



#an empty list
val2 = []
#checking if the number enterd is an integer
try:
#asking no o word that the user wants to add to the list
    num = int(input("enter how many words you want to add to the list\n"))
except ValueError:
    print ("not an integer")
for i in range(num):
    #printing positon of the word beind entered
    print("this is the", end=" ")
    print(i+1, end=" ")
    print("word you want to add")
    #Asking the user for the word they want to add to the list
    wordToApend = input("enter the word or number\n")
    #storing the return value in another list
    hi = appending(val2, wordToApend)
print("this is your list")
print(hi)
