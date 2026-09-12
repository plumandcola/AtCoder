N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A-1].append(B)
    g[B-1].append(A)

for i in range(N):
    g[i].sort()
    print(len(g[i]), *g[i])
