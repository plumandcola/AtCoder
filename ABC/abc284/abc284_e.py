import sys
sys.setrecursionlimit(10000000)

def dfs(v: int, visited: list[bool], result: int) -> int:
    if result >= 10 ** 6: #打ち切る
        return result

    result += 1
    for u in g[v]:
        if visited[u] == False:
            visited[u] = True
            result = dfs(u, visited, result)
            visited[u] = False
    return result


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

visited = [False] * N
visited[0] = True
print(min(dfs(0, visited, 0), 10 ** 6))