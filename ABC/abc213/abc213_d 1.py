import sys

sys.setrecursionlimit(1000000)

def dfs(v: int):
    ans.append(v + 1)
    for u in g[v]:
        if u not in visited:
            visited.add(u)
            dfs(u)
            ans.append(v + 1)


N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

for i in range(N):
    g[i].sort()

ans = []
visited = {0}
dfs(0)

print(*ans)