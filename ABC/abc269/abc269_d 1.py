from collections import deque


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
        q = deque([i])
        while q:
            v = q.popleft()
            for u in g[v]:
                if visited[u] == False:
                    visited[u] = True
                    q.append(u)

print(ans)