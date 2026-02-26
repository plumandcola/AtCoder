N, X = map(int, input().split())

dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    a, b = map(int, input().split())
    for j in range(X):
        if dp[i][j] == True:
            if j + a <= X:
                dp[i + 1][j + a] = True
                if j + b <= X:
                    dp[i + 1][j + b] = True

print("Yes" if dp[N][X] else "No")