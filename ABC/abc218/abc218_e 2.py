import heapq

N, M = map(int, input().split())

g = [[] for _ in range(N)]
s = 0 #辺の長さの和
for _ in range(M):
    A, B, C = map(int, input().split())
    g[A-1].append((B-1, C))
    g[B-1].append((A-1, C))
    if C > 0:
        s += C

visited = [False] * N
visited[0] = True
q = []
for u, c in g[0]:
    heapq.heappush(q, (c, u))

while q:
    c, v = heapq.heappop(q)
    if not visited[v]:
        visited[v] = True
        if c > 0:
            s -= c
        for u, c in g[v]:
            heapq.heappush(q, (c, u))

print(s)