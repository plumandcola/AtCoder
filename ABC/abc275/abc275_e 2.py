N, M, K = map(int, input().split())
mod = 998244353
M_inv = pow(M, mod - 2, mod)

dp = [[0] * (N+1) for _ in range(K+1)]
"""dp[i][j] := マスjからルーレットをあとi回まで回してゴールできる確率 % mod の累積和"""
dp[0][N] = 1

for i in range(K):
    for j in range(N):
        if j+M > N:
            dp[i+1][j] = (dp[i][N-1] - dp[i][2*N - j - M - 1] + dp[i][N] - dp[i][j]) % mod * M_inv % mod
        else:
            dp[i+1][j] = (dp[i][j+M] - dp[i][j]) % mod * M_inv % mod
    dp[i+1][N] = 1
    
    for j in range(N):
        dp[i+1][j+1] = (dp[i+1][j+1] + dp[i+1][j]) % mod #累積和

print(dp[K][0])