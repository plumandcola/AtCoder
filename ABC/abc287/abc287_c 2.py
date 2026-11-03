import sys
sys.setrecursionlimit(10000000)

def dfs(v: int):
    for u in g[v]:
        if not visited[u]:
            visited[u] = True
            dfs(u)


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)


ans = "Yes"

#辺がちょうどN-1本かどうか
if M != N-1:
    ans = "No"

#全ての頂点の次数が2以下かどうか
for i in range(N):
    if len(g[i]) > 2:
        ans = "No"

#グラフが連結かどうか
visited = [False] * N
dfs(0) #dfs(再帰)
for i in range(N):
    if not visited[i]:
        ans = "No"

print(ans)