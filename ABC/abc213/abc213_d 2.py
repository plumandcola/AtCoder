import heapq, sys

sys.setrecursionlimit(1000000)

def dfs(v: int, parent: int):
    ans.append(v + 1)
    while g[v]:
        u = heapq.heappop(g[v])
        if u != parent:
            dfs(u, v)
            ans.append(v + 1)


N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    heapq.heappush(g[A-1], B-1)
    heapq.heappush(g[B-1], A-1)

ans = []
dfs(0, -1)

print(*ans)