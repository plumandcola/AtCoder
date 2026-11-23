N = int(input())
mod = 998244353

A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [[0] * 2 for _ in range(N)]
"""
dp[i][0] := カードiまでの段階で、カードiが表の場合の数
dp[i][1] := カードiまでの段階で、カードiが裏の場合の数
"""
dp[0][0] = 1
dp[0][1] = 1
for i in range(1, N):
    dp[i][0] = (dp[i-1][0] * (A[i-1] != A[i]) + dp[i-1][1] * (B[i-1] != A[i])) % mod
    dp[i][1] = (dp[i-1][0] * (A[i-1] != B[i]) + dp[i-1][1] * (B[i-1] != B[i])) % mod

print(sum(dp[N-1]) % mod)