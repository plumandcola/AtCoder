N, M, K = map(int, input().split())

dp = [[0] * (K+2) for _ in range(N+1)]
"""dp[i][j] := 長さiで和がj-1以下の数列の個数(累積和)"""
for j in range(1, K+2):
    dp[0][j] = 1
for i in range(N):
    for j in range(1, K+2):
        dp[i+1][j] = (dp[i][j-1] - dp[i][max(0, j-M-1)] + dp[i+1][j-1]) % 998244353
        #dp[i+1][j]を求めつつ累積和も同時に求める

print(dp[N][K+1])