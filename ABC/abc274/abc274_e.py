N, M = map(int, input().split())

X = [0] * (N+M)
Y = [0] * (N+M)
for i in range(N+M):
    X[i], Y[i] = map(int, input().split())

d = [[0.0] * (N+M) for _ in range(N+M)]
for i in range(N+M):
    for j in range(N+M):
        d[i][j] = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** 0.5
        d[j][i] = d[i][j]

dp = [[float("inf")] * (N+M) for _ in range(1 << (N+M))]
"""dp[b][i] := 原点からスタートし、ビット列bで表される集合に含まれる全ての街と宝箱を巡って、街か宝箱iに到達するまでにかかる時間の最小値"""

#集合のサイズが1の場合
for i in range(N+M):
    dp[1 << i][i] = (X[i] ** 2 + Y[i] ** 2) ** 0.5

#集合のサイズを1つずつ大きくしていく
for b in range(1, 1 << (N+M)):
    for i in range(N+M):
        if (b >> i) & 1 == 0: continue

        for j in range(N+M):
            if (b >> j) & 1 == 1: continue
            dp[b | 1 << j][j] = min(dp[b | 1 << j][j], dp[b][i] + d[i][j] / 2 ** (b >> N).bit_count())

ans = float("inf")
for b in range(1 << M): #どの宝箱を訪れたか全探索
    b = (b << N) | ((1 << N) - 1) #街N個は全て訪れる必要があるので、下Nビットを立たせる
    for i in range(N+M):
        ans = min(ans, dp[b][i] + (X[i] ** 2 + Y[i] ** 2) ** 0.5 / 2 ** (b >> N).bit_count())

print(ans)