



def slist_to_string(list_to_convert):
    game = ""
    lenght = len(list_to_convert)
    print(lenght)
    for i in range(lenght):
        if i == lenght - 2:
            game += list_to_convert[i] + " and "
        elif i != lenght - 2:
            game += list_to_convert[i] + ',' + ' '
    return game









spam = ['apples', 'bananas', 'tofu', 'cats']
fantom = slist_to_string(spam)
print(fantom)



