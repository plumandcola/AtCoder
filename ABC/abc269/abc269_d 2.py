import sys
sys.setrecursionlimit(10000000)


def is_adjacent(x_i: int, y_i: int, x_j: int, y_j: int) -> bool:
    if x_i - 1 == x_j and y_i - 1 == y_j:
        return True
    elif x_i - 1 == x_j and y_i == y_j:
        return True
    elif x_i == x_j and y_i - 1 == y_j:
        return True
    elif x_i == x_j and y_i + 1 == y_j:
        return True
    elif x_i + 1 == x_j and y_i == y_j:
        return True
    elif x_i + 1 == x_j and y_i + 1 == y_j:
        return True
    
    return False


def dfs(v: int):
    for u in g[v]:
        if visited[u] == False:
            visited[u] = True
            dfs(u)


N = int(input())

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if is_adjacent(X[i], Y[i], X[j], Y[j]):
            g[i].append(j)
            g[j].append(i)

ans = 0
visited = [False] * N
for i in range(N):
    if visited[i] == False:
        ans += 1
        visited[i] = True
        dfs(i)

print(ans)