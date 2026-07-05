N = int(input())
A = list(map(int, input().split()))
mod = 998244353

dp = [0] * N #期待値DP
s = [0] * N #累積和(逆向き)
for i in range(N-2, -1, -1): #マスN-1から逆向きに
    s[i] = (s[i+1] + dp[i+1]) % mod
    #EV = (マスi+1〜i+A[i]までの期待値の合計 + A[i] + 1) / A[i]
    dp[i] = (s[i] - s[i + A[i]] + A[i] + 1) * pow(A[i], mod - 2, mod) % mod

print(dp[0])