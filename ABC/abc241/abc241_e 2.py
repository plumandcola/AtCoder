N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * N for _ in range(41)]
dp[0] = A[:]

ans = 0
i = 0
while K:
    for j in range(N):
        dp[i+1][j] = dp[i][j] + dp[i][(j + dp[i][j]) % N]
    if K & 1 == 1:
        ans += dp[i][ans % N]
    i += 1
    K >>= 1

print(ans)