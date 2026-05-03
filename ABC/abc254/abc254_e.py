from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    d = {x-1: 0}
    q = deque([x-1]) #bfs
    while q:
        v = q.popleft()
        for u in g[v]:
            if d[v] < k and u not in d:
                d[u] = d[v] + 1
                q.append(u)
    print(sum(i+1 for i in d))
