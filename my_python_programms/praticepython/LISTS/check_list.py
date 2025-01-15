




tableData = [['apples', 'oranges', 'cherries', 'banana'], 
 ['Alice', 'Bob', 'Carol', 'David'], 
 ['dogs', 'cats', 'moose', 'goose']]
print(tableData[0], tableData[1], tableData[2], tableData[2], tableData[1])
home = len(tableData)- 1
print(home)
for i in range(home):
    k =len(tableData[i]) - 1
    print(k)
    for v in range(k):
        
        print(tableData[v][i].ljust(6), end =' ')
    print('\n')
