N, M = map(int, input().split())

C = [0] * M
cost = [0] * M
p = [[0] * N for _ in range(M)]
for i in range(M):
    C[i], cost[i] = map(int, input().split())
    for j in range(C[i]):
        idol, p_ij = map(int, input().split())
        p[i][idol - 1] = p_ij

dp = [float("inf")] * (1 << N)
"""dp[b] := 集まっているアイドルがビット列bの状態から、すべてのアイドルを集めるために必要な金額の期待値"""
dp[-1] = 0

x = [[0] * M for _ in range(1 << N)]
y = [[0] * M for _ in range(1 << N)]
"""
期待値をEとして、E = xE + y
ただし誤差防止のために、全て100倍する
"""

for b in range((1 << N) - 2, -1, -1):
    for i in range(M):
        y[b][i] = cost[i] * 100
        for j in range(N):
            if p[i][j] != 0:
                if (b >> j) & 1 == 0:
                    y[b][i] += dp[b | (1 << j)] * p[i][j]
                else:
                    x[b][i] += p[i][j]
        
        if x[b][i] != 100:
            dp[b] = min(dp[b], y[b][i] / (100 - x[b][i]))

print(dp[0])