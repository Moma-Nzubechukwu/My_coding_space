







prompt = input('enter what you whant to sort')
if str(prompt).isdecimal():
    print (prompt, type(prompt), len(prompt))
#    prompt = int(prompt)
    for i in len(prompt):
        for v in len(prompt):
            if prompt[v] > prompt[v+1]:
                temp = prompt[v]
                promt[v] = prompt[v+1]
                prompt[v+1] = temp
print (prompt)

