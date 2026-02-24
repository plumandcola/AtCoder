import sys

sys.setrecursionlimit(10000000)

N, Q = map(int, input().split())
X = list(map(int, input().split()))

g = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

ans = [[X[i]] for i in range(N)]

def dfs(v, parent):
    for u in g[v]:
        if u != parent:
            dfs(u, v)
            ans[v] += ans[u]
    
    ans[v] = sorted(ans[v], reverse=True)[:20]

dfs(0, -1)

for _ in range(Q):
    V, K = map(int, input().split())
    print(ans[V-1][K-1])