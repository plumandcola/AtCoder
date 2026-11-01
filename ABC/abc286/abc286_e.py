N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]


d = [[float("inf")] * N for _ in range(N)]
s = [[0] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
    s[i][i] = A[i]
    for j in range(N):
        if S[i][j] == 'Y':
            d[i][j] = 1
            s[i][j] = A[i] + A[j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                s[i][j] = s[i][k] + s[k][j] - A[k]
            elif d[i][j] == d[i][k] + d[k][j]:
                s[i][j] = max(s[i][j], s[i][k] + s[k][j] - A[k]) #都市kのお土産が重複するので、引く


Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    if d[U][V] != float("inf"):
        print(d[U][V], s[U][V])
    else:
        print("Impossible")
