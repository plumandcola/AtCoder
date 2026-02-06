N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (b[-1] + 1) for _ in range(N+1)]
for j in range(b[-1] + 1):
    dp[0][j] = 1
for i in range(N):
    for j in range(a[i], b[i] + 1):
        dp[i+1][j] = dp[i][j]
    for j in range(b[-1]):
        dp[i+1][j+1] = (dp[i+1][j+1] + dp[i+1][j]) % 998244353

print(dp[N][b[-1]])