#30点解法
N, M = map(int, input().split())

dp = [0] * (1 << M)
for _ in range(N):
    l, r, s = map(int, input().split())
    B = ((1 << (r-l+1)) - 1) << (l-1)
    for b in range((1 << M) - 1, -1, -1):
        dp[b | B] = max(dp[b | B], dp[b] + s)

print(max(dp[:-1]))