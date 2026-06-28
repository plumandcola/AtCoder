N, M = map(int, input().split())
g = [[0] * N for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    g[U-1][V-1] = 1
    g[V-1][U-1] = 1

ans = 0
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            if g[a][b] == 1 and g[b][c] == 1 and g[c][a] == 1:
                ans += 1

print(ans)