#30点解法
import sys
sys.setrecursionlimit(10000000)

def dfs(v: int):
    for u in g[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            dfs(u)


N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    d = [-1] * N
    d[a-1] = 0
    dfs(a-1) #dfs(再帰)
    print(d[b-1] + 1)
