



prompt = input("enter\n")
name = ''
post = []
for i in range(len(prompt)):
    if prompt != ' ':
        name += prompt[i]
    post.append(name)
    name = ''
print(post)
