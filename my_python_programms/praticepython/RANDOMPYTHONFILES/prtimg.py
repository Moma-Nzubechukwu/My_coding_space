import pprint

grid =     [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
newlist = []
oldlist = []
for item in range(len(grid)):
    for subitems in range(len(grid[item])):
        for ran in range(len(grid[item][subitems])):
            newlist.append(grid[item][subitems][ran])

        print(newlist)

        oldlist.append(newlist)
        newlist = []
pprint.pprint(oldlist)
