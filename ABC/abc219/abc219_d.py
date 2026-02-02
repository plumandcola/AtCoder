N = int(input())
X, Y = map(int, input().split())

dp = [[[float("inf")] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
"""dp[i][j][k] := i種類目の弁当までで、j個のたこ焼きとk個のたい焼きを購入するのに必要なお弁当の最小値"""
dp[0][0][0] = 0
for i in range(N):
    A, B = map(int, input().split())
    for j in range(X+1):
        for k in range(Y+1):
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            dp[i+1][min(X, j+A)][min(Y, k+B)] = min(dp[i+1][min(X, j+A)][min(Y, k+B)], dp[i][j][k] + 1)

print(dp[N][X][Y] if dp[N][X][Y] != float("inf") else -1)