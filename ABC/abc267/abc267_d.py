N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-float("inf")] * (M+1) for _ in range(N+1)]
"""dp[i][j] := 長さjの、A[i]までの部分列に対する最大値"""
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        dp[i+1][j] = dp[i][j]
    for j in range(M):
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + (j+1) * A[i])

print(dp[N][M])