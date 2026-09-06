X = input()

for i in range(len(X)):
    if X[i] == 'o' or X[i] == 'k' or X[i] == 'u':
        continue
    if X[i] == 'c' and i+1 < len(X) and X[i+1] == 'h':
        continue
    if X[i] == 'h' and i-1 >= 0 and X[i-1] == 'c':
        continue
    
    print("NO")
    break
else:
    print("YES")
