list1 = [["name", 'address', 'phone no'],
        ["moma", "nzube", 'shadow', 'fransisco'],
        ['no 5 akpan street', 'no 7 oo street'],
        ['0901243456', '0807654123']]
list2 = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'K', 'L', 'M', 'N', 'O', "P", "Q", "R", "S", 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(list1)
print('\t\n ok \t\n')
for i in range(len(list1)):
    for g in range(len(list1[i])):
            print (list1[i][g])
print(list1[0:2])
print(list3, len(list3))
print(list1 + list2 + list3)
#del list1[0]
print(list1)
if "a" in list3:
    print('hi')
else:
    print('do 5his')
print(list2.index(1))
list2.sort(reverse = True)
print(list2)
