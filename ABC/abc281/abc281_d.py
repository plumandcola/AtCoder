N, K, D = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-float("inf")] * D for _ in range(K+1)]
"""dp[j][r] := j個の項の和をDで割った余りがrの時の、和の最大値"""
dp[0][0] = 0
for i in range(N):
    for j in range(K, 0, -1):
        for r in range(D):
            dp[j][(r + a[i]) % D] = max(dp[j][(r + a[i]) % D], dp[j-1][r] + a[i])

print(dp[K][0] if dp[K][0] != -float("inf") else -1)