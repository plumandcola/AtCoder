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
q = [0] #dfs(スタック)
while q:
    v = q.pop()
    for u in g[v]:
        if visited[u] == False:
            visited[u] = True
            q.append(u)
for i in range(N):
    if not visited[i]:
        ans = "No"

print(ans)