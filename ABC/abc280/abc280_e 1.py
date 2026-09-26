N, P = map(int, input().split())
mod = 998244353

inv_100 = pow(100, mod - 2, mod)

dp = [0] * (N+1)
"""dp[i] := モンスターの体力がiの状態から、モンスターの体力が0以下になるまでに行う攻撃回数の期待値 % mod"""
dp[1] = 1
for i in range(2, N+1):
    dp[i] = (1 + dp[i-2] * P % mod * inv_100 % mod + dp[i-1] * (100 - P) % mod * inv_100 % mod) % mod

print(dp[N])