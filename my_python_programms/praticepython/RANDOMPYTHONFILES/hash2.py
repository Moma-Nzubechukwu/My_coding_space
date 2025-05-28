


def myhash(prompt, s_no):
    strToHash = list(prompt)
    for i in range(len(strToHash)):
        strToHash[i] = chr(ord(strToHash[i])* s_no)
    return ''.join(strToHash)
print(myhash(input("\n"), 100))

