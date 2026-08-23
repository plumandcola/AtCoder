#30点解法
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

dp = [[float("inf")] * (H + N*B + 1) for _ in range(N+1)] #満腹度の上限は、H + N*B
dp[0][H] = 0
for i in range(N): #i日目
    for h in range(H + N*B + 1): #満腹度h
        if dp[i][h] == float("inf"): continue #i日目に満腹度がhであることは不可能

        dp[i+1][h+B] = min(dp[i+1][h+B], dp[i][h] + A)
        dp[i+1][h+D] = min(dp[i+1][h+D], dp[i][h] + C)
        if h > E: #h-E > 0なら
            dp[i+1][h-E] = min(dp[i+1][h-E], dp[i][h])

print(min(dp[N]))