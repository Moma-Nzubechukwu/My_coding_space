





num1 = input("enter what you want to sort\n")
randDic = num1.split(',')
print("this is what you entered", randDic)
#randDic = [1,74,63,83,83,73,74,74,94,83,84,83,73,3,73]
for y in range(len(randDic)- 1):
    for i in range(len(randDic) - 1):
        if randDic[i] > randDic[i + 1]:
#            print(i)
            temp = randDic[i]
            randDic[i] = randDic[i + 1]
            randDic[i + 1] = temp
print (randDic)
