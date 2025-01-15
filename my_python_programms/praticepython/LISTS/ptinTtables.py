def printTable(listOflist):
    no_of_list = len(listOflist)
    
    v = len(listOflist)
 #   print(v)

#    sub = len(listOflist[1])
#    print('hi', v)
    for k in range(v + 1):
        sub = len(listOflist[k])
#        print(sub)
        for i in range(sub):
         #   print('i:', i)
            name = listOflist[i][k].rjust(8)
            print (name, end=' ')
        print('\n')
#    listOflist = 0





tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
