H, W = map(int, input().split())
C = [input() for _ in range(H)]

dp = [[-float("inf")] * (W+1) for _ in range(H+1)]
dp[1][1] = 1
for i in range(H):
    for j in range(W):
        if C[i][j] != '#':
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1] + 1, dp[i+1][j] + 1)

print(max(max(dp[i]) for i in range(H+1)))