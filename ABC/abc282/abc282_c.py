N = int(input())

enclosed = False
for c in input():
    if c == '"':
        enclosed ^= True
    
    if c == ',' and enclosed == False:
        print('.', end="")
    else:
        print(c, end="")
print() #改行