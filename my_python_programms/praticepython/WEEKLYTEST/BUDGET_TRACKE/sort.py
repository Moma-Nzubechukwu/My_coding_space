
# a sortimg algorithim






prompt = input('enter what you whant to sort')
if str(prompt).isdecimal():
    print (prompt, type(prompt), len(prompt))
#    prompt = int(prompt)
    for i in range(len(prompt)):
        for v in range(len(prompt)):
            if prompt[v] > prompt[v+1]:
                temp = prompt[v]
                prompt[v] = prompt[v+1]
                prompt[v+1] = temp
print (prompt)

