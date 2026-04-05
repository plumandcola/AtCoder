import heapq

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    g[A-1].append((B-1, C, i+1))
    g[B-1].append((A-1, C, i+1))

ans = []
visited = [False] * N
q = [(0, 0, 0)]
while q:
    C, v, i = heapq.heappop(q)
    if not visited[v]:
        visited[v] = True
        ans.append(i)
        for u, c, i in g[v]:
            if not visited[u]: #なくてもACにはなるが、時間ギリギリ
                heapq.heappush(q, (C + c, u, i))

print(*ans[1:]) #最初の0は出力しない