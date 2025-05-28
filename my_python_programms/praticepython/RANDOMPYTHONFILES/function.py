def invert(promptToInvert):
    n = len(promptToInvert)
    promptlist = list(promptToInvert)
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




def myhash(prompt, s_no=12):
    strToHash = list(prompt)
    for i in range(len(strToHash)):
        strToHash[i] = chr(ord(strToHash[i])* s_no)
    return ''.join(strToHash)


def myunhash(strtounhash, s_no = 12):
    strToHash = list(strtounhash)
    for i in range(len(strToHash)):
        strToHash[i] = chr(int(ord(strToHash[i])/ s_no))
    return ''.join(strToHash)
