import sys

sys.setrecursionlimit(1000000)

def dfs(v: int, parent: int) -> bool:
    ans = True
    for u in g[v]:
        if u != parent:
            if visited[u] == True: #閉路あり
                ans = False
            else:
                visited[u] = True
                dfs(u, v)
    return ans


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

ans = True
visited = [False] * N
for i in range(N):
    if len(g[i]) > 2: #隣り合わないといけない人が2人を超えるなら不可能
        ans &= False
        break
    
    if visited[i] == True:
        continue
    
    ans &= dfs(i, -1)

print("Yes" if ans else "No")