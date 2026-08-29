#30点解法
N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    d = [-1] * N
    d[a-1] = 0
    q = [a-1] #dfs(スタック)
    while q:
        v = q.pop()
        for u in g[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                q.append(u)

    print(d[b-1] + 1)
