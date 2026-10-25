#50点解法
N, M, T = map(int, input().split())
A = list(map(int, input().split()))

d = [[float("inf")] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c

#ワーシャルフロイド法
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for i in range(N):
    ans = max(ans, A[i] * (T - d[0][i] - d[i][0]))

print(ans)