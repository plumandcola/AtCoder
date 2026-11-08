N = int(input())
a = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = 0
for i in range(N-1):
    dp[i+1] = min(dp[i+1], dp[i] + abs(a[i+1] - a[i]))
    if i+2 < N:
        dp[i+2] = min(dp[i+2], dp[i] + abs(a[i+2] - a[i]))

print(dp[N-1])