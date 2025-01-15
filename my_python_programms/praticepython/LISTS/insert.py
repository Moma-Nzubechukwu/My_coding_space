





game = ['call of duty', "free fire", 'freedom fighter', 'genshi impact']


rash = game[1]
print (game)
hi = input('enter a game')
game.insert(1, hi)
print(game)
del game[1]
game.remove("freedom fighter")
print(game)
game.append(rash)
game.sort(key = str.lower)
print(game)
