



prompt = input("enter\n")
name = ''
post = []
for y in range(len(prompt)):
    for i in range(y, len(prompt)):
        if prompt != ' ':
            name += prompt[i]
        else:
            break
    post.append(name)
    print(name)
    name = ''
print(post)
