import sys
sys.setrecursionlimit(10000000)

def dfs(v: int, parent: int, visited: list[int]):
    if v == Y:
        print(*visited)
    
    for u in g[v]:
        if u != parent:
            visited.append(u)
            dfs(u, v, visited)
            visited.pop()


N, X, Y = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    g[U].append(V)
    g[V].append(U)

dfs(X, -1, [X])