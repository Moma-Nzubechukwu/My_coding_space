"""
this is a script that inverts evry thing you input in it
*promptToIvert - stores what the user enterd 
*n - lenght of promptToInvert
*promptlist - a list of all the character in the inputed string 

"""



def invert(promptToInvert):
    n = len(promptToInvert)
    promptlist = list(promptToInvert)
#    print(promptlist)
    i = 0
    g = n - 1
    while (i < (n - 1)/2 and g > (n - 1)/2):
        #loops and swap an index with the coresponding index at the end
#        print(i, g, sep = ",")
        temp = promptlist[i]
        yemp = promptlist[g]
        promptlist[i] = yemp
        promptlist[g] = temp
        i = i + 1
        g = g - 1
    return (str(''.join(promptlist)))

