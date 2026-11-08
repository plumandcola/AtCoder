#50点解法
from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, y = map(int, input().split())
    g[a-1].append((b-1, y))
    g[b-1].append((a-1, y))

Q = int(input())
for _ in range(Q):
    ans = 1
    v, w = map(int, input().split())
    q = deque([v-1]) #bfs
    visited = [False] * N
    visited[v-1] = True
    while q:
        v = q.popleft()
        for u, y in g[v]:
            if y > w and visited[u] == False:
                visited[u] = True
                ans += 1
                q.append(u)
    print(ans)
