S = ["............"] + ["." + input() + "." for _ in range(10)] + ["............"]

for i in range(1, 11):
    for j in range(1, 11):
        if S[i-1][j-1] == '.' and S[i-1][j] == '.' and S[i][j-1] == '.' and S[i][j] == '#':
            A = i
            C = j
        if S[i][j] == '#' and S[i][j+1] == '.' and S[i+1][j] == '.' and S[i+1][j+1] == '.':
            B = i
            D = j

print(A, B)
print(C, D)