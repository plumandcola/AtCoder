N, Q = map(int, input().split())

L = [0] * N
a = [[] for _ in range(N)]
for i in range(N):
    L[i], *a[i] = map(int, input().split())

for _ in range(Q):
    s, t = map(int, input().split())
    print(a[s-1][t-1])
