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
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)


count = 0 #連結成分の個数
visited = [False] * N
for i in range(N):
    if visited[i] == False:
        count += 1
        dfs(i) #dfs(再帰)

print(M - N + count)