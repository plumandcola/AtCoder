N = int(input())

x = [0] * N
y = [0] * N
P = [0] * N
for i in range(N):
    x[i], y[i], P[i] = map(int, input().split())

d = [[float("inf")] * N for _ in range(N)]
"""d[i][j] := i番目のジャンプ台からj番目のジャンプ台にジャンプするのに必要な訓練の回数"""
for i in range(N):
    for j in range(N):
        d[i][j] = (abs(x[i] - x[j]) + abs(y[i] - y[j]) + P[i] - 1) // P[i]

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], max(d[i][k], d[k][j]))

print(min(max(d[i]) for i in range(N)))