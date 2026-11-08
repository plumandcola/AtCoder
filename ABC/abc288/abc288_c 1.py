from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)


count = 0 #連結成分の個数
visited = [False] * N
for i in range(N):
    if visited[i] == False:
        count += 1
        q = deque([i]) #bfs
        while q:
            v = q.popleft()
            for u in g[v]:
                if visited[u] == False:
                    visited[u] = True
                    q.append(u)

print(M - N + count)