import sys
sys.setrecursionlimit(10000000)

def dfs(v: int, count: int) -> bool:
    if len(g[v]) >= 3 or (len(g[v]) == 1 and 1 < count < N): return False
    if count == N and len(g[v]) == 1: return True

    visited[v] = True
    for u in g[v]:
        if visited[u] == True: continue

        return dfs(u, count + 1)
    return False


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)


visited = [False] * N
for i in range(N):
    if len(g[i]) == 1 and dfs(i, 1):
        print("Yes")
        break
else:
    print("No")
