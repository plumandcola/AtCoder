#100点解法
import heapq

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

g = [[] for _ in range(N)]
g_r = [[] for _ in range(N)] #逆向き
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a-1].append((b-1, c))
    g_r[b-1].append((a-1, c))

def dijkstra(g: list[list[list[int]]]) -> list[int]:
    d = [float("inf")] * N
    d[0] = 0
    q = [(0, 0)]
    while q:
        C, v = heapq.heappop(q)
        if d[v] > C: continue

        for u, c in g[v]:
            C_new = C + c
            if d[u] > C_new:
                heapq.heappush(q, (C_new, u))
                d[u] = C_new
    return d

#ダイクストラ法
d = dijkstra(g)
d_r = dijkstra(g_r) #逆向き

ans = 0
for i in range(N):
    if d[i] != float("inf") and d_r[i] != float("inf") and d[i] + d_r[i] <= T:
        ans = max(ans, A[i] * (T - d[i] - d_r[i]))

print(ans)