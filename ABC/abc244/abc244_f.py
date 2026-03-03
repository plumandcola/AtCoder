from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

dp = [[float("inf")] * N for _ in range(1 << N)]
for i in range(N):
    dp[0][i] = 0
q = deque()
for i in range(N):
    dp[1 << i][i] = 1
    q.append(((1 << i), i))
while q:
    b, v = q.popleft()
    for u in g[v]:
        B = b ^ (1 << u)
        if dp[B][u] == float("inf"):
            dp[B][u] = dp[b][v] + 1
            q.append((B, u))

print(sum(min(dp[b]) for b in range(1 << N)))