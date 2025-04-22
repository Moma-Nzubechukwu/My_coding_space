import copy


def changepar(ok):
    ok[3] = 500000000




list1 = [1,2,3,4,5,6,7,8,9,0]
print(list1)
changepar(copy.copy(list1))
print((list1))

