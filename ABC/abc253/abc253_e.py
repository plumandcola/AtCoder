N, M, K = map(int, input().split())

dp = [[0] * (M+1) for _ in range(N)] #場合の数の累積和
for j in range(M+1):
    dp[0][j] = j

for i in range(N-1):
    for j in range(1, M+1):
        if K != 0:
            dp[i+1][j] = ((dp[i][max(0, j-K)] - dp[i][0]) + (dp[i][M] - dp[i][min(M, j+K-1)])) % 998244353
        else:
            dp[i+1][j] = (dp[i][M] - dp[i][0]) % 998244353
        dp[i+1][j] = (dp[i+1][j] + dp[i+1][j-1]) % 998244353 #累積和を取る

print(dp[N-1][M])