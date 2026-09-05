N, M = map(int, input().split())

d = [[float("inf")] * N for _ in range(N)]
"""d[i][j] := i番目の人からj番目の人までの最短距離"""
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    A, B = map(int, input().split())
    d[A-1][B-1] = 1
    d[B-1][A-1] = 1

#ワーシャルフロイド法
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(N):
    print(sum(d[i][j] == 2 for j in range(N)))
