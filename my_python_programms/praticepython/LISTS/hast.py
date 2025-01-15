

alphabets = ["A","B","c,","a","b"]
alphabets.sort(key=str.lower)
print(alphabets)
alphabets.sort(reverse=True, key=str.upper)
print(alphabets)

