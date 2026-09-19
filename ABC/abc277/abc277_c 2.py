from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

def dfs(v: int):
    for u in g[v]:
        if u not in visited:
            visited.add(u)
            dfs(u)


N = int(input())

g = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

visited = {1}
dfs(1) #dfs(再帰)

print(max(visited))