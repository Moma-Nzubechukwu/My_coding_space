


# moma  mzube
def space_remover(data):
    gash = ''
    g = 0
    for i in range(len(data)):
        if data[i] != ' ':
            gash += data[i]
        elif data[i] == ' ' and g > 1:
#            continue
            print(end = '')
        if data[i] == ' ' and g == 0:
            gash += data[i]
#            print(i)
        if data[i]== ' ' and data[i + 1] != ' ':
 #           print()
            g = 0
            continue
        if data[i] == ' ' and data[i + 1] == ' ':
            g = g + 1
    gash = gash.strip()
    return gash 




fileobj = open("file.txt", 'r')
newfile = fileobj.read()
name = space_remover(newfile)
gash = open('new file.txt', 'a')
gash.write(name)
print(name)
print(len(name))
