import heapq

N, M = map(int, input().split())

d = [[float("inf")] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    a, b, t = map(int, input().split())
    d[a-1][b-1] = min(d[a-1][b-1], t)
    d[b-1][a-1] = min(d[b-1][a-1], t)

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = float("inf")
for i in range(N):
    ans = min(ans, max(d[i]))

print(ans)