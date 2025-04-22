#strimg manipulation



name = "momanzube1234".upper()
print(name)
if name.isupper():
    name = name.lower()
    print(name)
prompt = input('enter something')
if prompt.isalpha():
    print("contains alphabets only")
if prompt.isalnum():
    print("contains alpjanets and numbers")
if prompt.isspace():
    print('''
    it contains 1 of these
    - new line
    - tab
    - white space

            ''')
if prompt.isdecimal():
    print('it contain integers(numbers)')
if prompt.istitle():
    print("all characters except the first character are small letters")
if prompt.startswith('a'):
    print('starts with a')
if prompt.endswith('z'):
    print('endswith z')

    

