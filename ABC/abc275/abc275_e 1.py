N, M, K = map(int, input().split())
mod = 998244353
M_inv = pow(M, mod - 2, mod)

dp = [[0] * (N+1) for _ in range(K+1)]
"""dp[i][j] := マスjからルーレットをあとi回まで回してゴールできる確率 % mod"""
dp[0][N] = 1

for i in range(K):
    for j in range(N):
        for k in range(1, M+1):
            J = min(j + k, 2*N - j - k) #マスjで目kが出た時に移動する先のマス
            dp[i+1][j] = (dp[i+1][j] + dp[i][J] * M_inv) % mod
    dp[i+1][N] = 1

print(dp[K][0])