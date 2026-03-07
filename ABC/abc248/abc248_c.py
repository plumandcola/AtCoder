N, M, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(K+1):
        dp[i+1][j] = sum(dp[i][max(0,j-M):j]) % 998244353

print(sum(dp[N]) % 998244353)