N = int(input())
a = list(map(int, input().split()))
mod = 998244353

dp = [[[0] * (N+1) for m in range(N+1)] for j in range(N+1)]
"""dp[j][m][r] := 項をj個選んで、mで割った余りがrとなる選び方 % mod"""
for m in range(1, N+1):
    dp[0][m][0] = 1

for i in range(N):
    for j in range(N, 0, -1):
        for m in range(1, N+1):
            for r in range(m):
                dp[j][m][(r + a[i]) % m] = (dp[j][m][(r + a[i]) % m] + dp[j-1][m][r]) % mod

print(sum(dp[j][j][0] for j in range(1, N+1)) % mod)