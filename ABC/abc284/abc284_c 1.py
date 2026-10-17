from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

ans = 0
visited = [False] * N
for i in range(N):
    if visited[i] == False:
        visited[i] = True
        ans += 1
        q = deque([i]) #bfs
        while q:
            v = q.popleft()
            for u in g[v]:
                if visited[u] == False:
                    visited[u] = True
                    q.append(u)

print(ans)