#30点解法
R, C, K = map(int, input().split())
s = [input() for _ in range(R)]

ans = 0
for x in range(K-1, R-K+1):
    for y in range(K-1, C-K+1):
        flag = True
        for i in range(R):
            for j in range(C):
                if abs(i-x) + abs(j-y) <= K-1 and s[i][j] == 'x':
                    flag = False
        if flag:
            ans += 1

print(ans)