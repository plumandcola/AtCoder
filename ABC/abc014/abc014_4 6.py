#100点解法
import sys
sys.setrecursionlimit(50000000)


N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)


parent = [0] * N
depth = [0] * N
size = [1] * N #部分木の大きさ

#dfs 1回目 部分木の大きさを求め、heacy childを求める
def dfs1(v: int, p: int):
    if len(g[v]) >= 2 and g[v][0] == p:
        g[v][0], g[v][-1] = g[v][-1], g[v][0] #vの親はg[v]の2番目以降へ
    for i in range(len(g[v])):
        u = g[v][i]
        if u == p: continue
        parent[u] = v
        depth[u] = depth[v] + 1
        dfs1(u, v)
        size[v] += size[u]
        if size[u] > size[g[v][0]]:
            g[v][0], g[v][i] = g[v][i], g[v][0] #heavy childを、g[v]の先頭へ

dfs1(0, -1)


head = [0] * N #head[v] := vを通るheavy pathの先頭（最も根側にある頂点）
id = [0] * N #id[v] := 行きがけ順で何番目にvを訪れるか
# vertex = [0] * N #vertex[i] := 行きがけ順でi番目に訪れる頂点

#dfs 2回目
def dfs2(v: int, p: int):
    global k
    for u in g[v]:
        if u == p: continue
        head[u] = head[v] if u == g[v][0] else u #uがvのheavy childならhead[u] = head[v]、そうでないならhead[u] = u
        id[u] = k
        # vertex[k] = u
        k += 1
        dfs2(u, v)

k = 1
dfs2(0, -1)


def LCA(a: int, b: int) -> int:
    while head[a] != head[b]:
        if id[a] > id[b]: a, b = b, a
        b = parent[head[b]]
    return a if id[a] < id[b] else b


Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    p = LCA(a, b)

    print((depth[a] - depth[p]) + (depth[b] - depth[p]) + 1)
