#50点解法
import sys
sys.setrecursionlimit(10000000)

def dfs(v: int, w: int):
    for u, y in g[v]:
        if y > w and visited[u] == False:
            visited[u] = True
            dfs(u, w)

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, y = map(int, input().split())
    g[a-1].append((b-1, y))
    g[b-1].append((a-1, y))

Q = int(input())
for _ in range(Q):
    v, w = map(int, input().split())
    visited = [False] * N
    visited[v-1] = True
    dfs(v-1, w) #dfs(再帰)
    print(sum(visited))
