
#this code prints the fabinachi series up to a limit 


#entering where to stop
maximum = int(input("enter the maximum no of fabinachi you want to print  "))
#initializimg the first 2 varriable
a = 0
b = 1
# a while loop to make sure it dose not pass the maximum number entered 
while b < maximum:
  #  storing in a temporary variable 
    c = a
    d = b
    a = b
    #adding the content of the temporary variable  and storing it ok n b
    b = c + d
    # printing b
    print(b)
