name = 'gash'
whatToCheck = 'gash        kdgash'

# Iterate through each character in `whatToCheck`
for t in range(len(whatToCheck)):
    if name[0] == whatToCheck[t]:  # Check if the first character of `name` matches
        print(t, whatToCheck[t])
        
        # Check for substring match
        for h in range(1, len(name) + 1):  # Incrementally check substrings of `name`
            if whatToCheck[t:t + h] == name[:h]:
                print(f"Match: {whatToCheck[t:t + h]}")
                man = whatToCheck[t:t + h]
            else:
                break
print(man)
