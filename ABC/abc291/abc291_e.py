N, M = map(int, input().split())

g_in = [set() for _ in range(N)]
g_out = [set() for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    g_out[X-1].add(Y-1)
    g_in[Y-1].add(X-1)

for i in range(N):
    if len(g_in[i]) == 0:
        q = [i]
        visited = []
        while q:
            v = q.pop()
            visited.append(v)
            for u in g_out[v]:
                g_in[u].remove(v)
                if len(g_in[u]) == 0:
                    q.append(u)
            
            if len(q) > 1:
                break
        
        if len(visited) == N:
            print("Yes")

            ans = [0] * N
            for i in range(N):
                ans[visited[i]] = i+1
            print(*ans)
        else:
            print("No")
        
        break
