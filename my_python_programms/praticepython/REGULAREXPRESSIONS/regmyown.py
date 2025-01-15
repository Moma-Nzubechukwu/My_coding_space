



name = 'gash'
whatToCheck = 'a        kdgash'
index = whatToCheck.index(name[0])
for t in range(len(whatToCheck)):
    if name[0] == whatToCheck[t]:
       print(t, whatToCheck[t])
       for h in range(t, len(whatToCheck)):
           j = 0
           h += 1
           print(h, 'h')
           m = 0
           if name[:h] == whatToCheck[t:h]:
               print(whatToCheck[t:h])
               print('name[:h]', name[:t])
               j += 1
           #    m = h + 1
           else:
                break


#for i in range(index, len(name)):
#    gash = gash + name[i]
