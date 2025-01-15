spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)
spam.setdefault('coulor', 'white')
print(spam)
