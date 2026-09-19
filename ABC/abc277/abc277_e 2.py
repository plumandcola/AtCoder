import heapq

N, M, K = map(int, input().split())

g = [[] for _ in range(2*N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    g[u-1 + a*N].append((v-1 + a*N, 1))
    g[v-1 + a*N].append((u-1 + a*N, 1))

for s in map(int, input().split()):
    g[s-1].append((s-1 + N, 0))
    g[s-1 + N].append((s-1, 0))

d = [float("inf")] * (2*N)
q = [(0, N)]
while q:
    W, v = heapq.heappop(q)
    if d[v] != float("inf"): continue

    d[v] = W
    for u, w in g[v]:
        if d[u] == float("inf"):
            heapq.heappush(q, (W + w, u))

ans = min(d[N-1], d[2*N - 1])
print(ans if ans != float("inf") else -1)