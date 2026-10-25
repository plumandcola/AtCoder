import heapq

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(1, M+1):
    A, B, C = map(int, input().split())
    g[A-1].append((B-1, C, i))
    g[B-1].append((A-1, C, i))

#ダイクストラ法
ans = []
d = [float("inf")] * N
d[0] = 0
q = [(0, 0, 0)] #(都市1からの距離, 都市の番号, 道路の番号)
while q:
    C, v, i = heapq.heappop(q)
    if d[v] < C: continue

    ans.append(i)
    for u, c, i in g[v]:
        C_new = C + c
        if d[u] > C_new:
            heapq.heappush(q, (C_new, u, i))
            d[u] = C_new

print(*ans[1:]) #最初の0は出力しない