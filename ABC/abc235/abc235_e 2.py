import heapq

N, M, Q = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a-1].append((b-1, c, -1)) #-1は、クエリではないことを表す
    g[b-1].append((a-1, c, -1)) #-1は、クエリではないことを表す

for i in range(Q):
    u, v, w = map(int, input().split())
    g[u-1].append((v-1, w, i)) #iは、何番目のクエリかを表す
    g[v-1].append((u-1, w, i)) #iは、何番目のクエリかを表す

ans = [False] * Q
visited = [False] * N
q = [(0, 0, -1)]
while q:
    C, v, i = heapq.heappop(q)
    if i == -1:
        if not visited[v]:
            visited[v] = True
            for u, c, i in g[v]:
                heapq.heappush(q, (c, u, i))
    else:
        if not visited[v]:
            ans[i] = True

for i in range(Q):
    print("Yes" if ans[i] else "No")