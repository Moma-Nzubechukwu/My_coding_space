



prompt = input("enter\n") 
name = ''
post = []
for i in range(len(prompt)):
    if prompt[i] != ' ':
        name += prompt[i]
    else:
        post.append(name)
        name = ''
        continue
post.append(name)
print(post)
