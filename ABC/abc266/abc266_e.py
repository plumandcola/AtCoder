N = int(input())

dp = [0.0] * (N+1)
for i in range(N):
    for j in range(1, 7):
        if j > dp[i]:
            dp[i+1] += j
        else:
            dp[i+1] += dp[i]
    dp[i+1] /= 6

print(dp[N])