from collections import defaultdict

#40点解法
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

dp = [defaultdict(lambda: float("inf")) for _ in range(N+1)]
dp[0][H] = 0
for i in range(N):
    for h in dp[i]:
        dp[i+1][h+B] = min(dp[i+1][h+B], dp[i][h] + A)
        dp[i+1][h+D] = min(dp[i+1][h+D], dp[i][h] + C)
        if h-E > 0:
            dp[i+1][h-E] = min(dp[i+1][h-E], dp[i][h])

print(min(dp[N].values()))