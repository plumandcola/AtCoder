import sys
sys.setrecursionlimit(10000000)

def dfs(v: int) -> bool:
    bipartite = True
    for u in g[v]:
        if color[u] == color[v]:
            bipartite = False
        elif color[u] == -1:
            color[u] = color[v] ^ 1
            count[color[u]] += 1
            bipartite &= dfs(u)
    
    return bipartite


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

ans = N * (N-1) // 2 - M #すべての頂点の組の数 - すでにある辺の数
color = [-1] * N #color[i] := 頂点iに塗る色
bipartite = True #Gが二部グラフかどうか
for i in range(N):
    if color[i] == -1: #頂点iが未訪問なら
        color[i] = 0
        count = [1, 0] #count[c] := 色cを塗った頂点の数
        bipartite &= dfs(i) #dfs(再帰)
        ans -= count[0] * (count[0] - 1) // 2 + count[1] * (count[1] - 1) // 2

print(ans if bipartite else 0)