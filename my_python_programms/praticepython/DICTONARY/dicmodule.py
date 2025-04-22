from pprint import *
myDic = {'name':'Moma Nzubechukwu', 'school':'University Of Niheria Nsukka', "age":18, 'complextion': 'dark', 'gender':'boy'}
print(myDic.items(), 'items')
"""
print(myDic.values(), 'values', type(myDic.values))
print(myDic.keys(), 'keys')
"""
if input("enter") in myDic.keys():
    print(myDic.get('age', 0))
    prompt, value = input("enter key"), input("enter value")
    print(myDic.setdefault(prompt, value))
    print("yes")
    print(myDic)
pprint(myDic)
print(type(pformat(myDic)))
