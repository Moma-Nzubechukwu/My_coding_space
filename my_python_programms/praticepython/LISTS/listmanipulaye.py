


list1 = [1,4,2,23,23,45,34,56,56,899,2,3,4,5,6,7,8,9,10]
print(list1);
if 1 in list1:
        print(list1)
for i in range(len(list1)):
    pass
#    print(list1[i:].index(3))
list1.insert(1, 75)
print(list1)
list1.remove(75)
print(list1)
list1.sort(reverse = True)
print(list1)
name = []
for z in range(33,127):
    name.append(chr(z))
print(name)
name.sort(key = str.upper)

print (name)
