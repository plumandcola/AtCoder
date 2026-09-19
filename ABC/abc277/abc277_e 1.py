from collections import deque

N, M, K = map(int, input().split())

g = [[] for _ in range(2*N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    g[u-1 + a*N].append(v-1 + a*N)
    g[v-1 + a*N].append(u-1 + a*N)

for s in map(int, input().split()):
    g[s-1].append(s-1 + N)
    g[s-1 + N].append(s-1)

d = [float("inf")] * (2*N)
d[N] = 0
q = deque([N])
while q:
    v = q.popleft()
    for u in g[v]:
        if u % N != v % N: #移動
            if d[u] == float("inf"):
                d[u] = d[v] + 1
                q.append(u)
        else: #スイッチを押す
            if d[u] > d[v]:
                d[u] = d[v]
                q.appendleft(u)

ans = min(d[N-1], d[2*N - 1])
print(ans if ans != float("inf") else -1)