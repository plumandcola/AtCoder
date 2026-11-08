N = int(input())
x = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(9):
        if x[i][j] == "x" or (x[i][j] == "o" and (i == 0 or x[i-1][j] != "o")):
            ans += 1

print(ans)