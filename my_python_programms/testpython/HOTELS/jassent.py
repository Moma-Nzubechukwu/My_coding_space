

#this is a code that sepreats each word of a sentence  and stores it in a list data type

def spaceList(prompt):
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
    #print(post)
    return post
