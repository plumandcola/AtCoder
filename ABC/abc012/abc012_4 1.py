import heapq

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    g[a-1].append((b-1, t))
    g[b-1].append((a-1, t))

ans = float("inf")
for i in range(N): #i番目のバス停に引っ越した際
    #ダイクストラ法
    time = [float("inf")] * N
    time[i] = 0
    q = [(0, i)]
    while q:
        T, v = heapq.heappop(q)
        if time[v] < T: continue

        for u, t in g[v]:
            T_new = T + t
            if time[u] > T_new:
                heapq.heappush(q, (T_new, u))
                time[u] = T_new
    ans = min(ans, max(time))

print(ans)