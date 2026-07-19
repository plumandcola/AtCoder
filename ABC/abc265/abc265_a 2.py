X, Y, N = map(int, input().split())

dp = [0] * (N+1)
for i in range(1, N+1):
    if i < 3:
        dp[i] = dp[i-1] + X
    else:
        dp[i] = min(dp[i-1] + X, dp[i-3] + Y)

print(dp[N])