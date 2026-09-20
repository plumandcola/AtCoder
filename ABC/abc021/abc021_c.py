from collections import deque

N = int(input())
a, b = map(int, input().split())

g = [[] for _ in range(N)]
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

ans = [0] * N
ans[a-1] = 1
d = [-1] * N
d[a-1] = 0
q = deque([a-1])
mod = 1000000007
while q:
    v = q.popleft()
    for u in g[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            ans[u] = (ans[u] + ans[v]) % mod
            q.append(u)
        elif d[u] == d[v] + 1:
            ans[u] = (ans[u] + ans[v]) % mod

print(ans[b-1])