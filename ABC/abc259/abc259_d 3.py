from collections import deque

N = int(input())
s_x, s_y, t_x, t_y = map(int, input().split())

x = [0] * N
y = [0] * N
r = [0] * N
for i in range(N):
    x[i], y[i], r[i] = map(int, input().split())
    if (s_x - x[i]) ** 2 + (s_y - y[i]) ** 2 == r[i] ** 2:
        s_i = i
    if (t_x - x[i]) ** 2 + (t_y - y[i]) ** 2 == r[i] ** 2:
        t_i = i

g = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        if (r[i] - r[j]) ** 2 <= (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= (r[i] + r[j]) ** 2:
            g[i].append(j)
            g[j].append(i)

#bfs
visited = [False] * N
q = deque([s_i])
while q:
    v = q.popleft()
    if visited[v] == True: continue
    
    visited[v] = True
    for u in g[v]:
        if visited[u] == False:
            q.append(u)

print("Yes" if visited[t_i] == True else "No")