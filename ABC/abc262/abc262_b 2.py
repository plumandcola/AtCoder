N, M = map(int, input().split())
g = [set() for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    g[U-1].add(V-1) #a<b<cの条件を満たすために、U→Vのみにする

ans = 0
for a in range(N-2):
    for b in g[a]:
        for c in g[b]:
            if c in g[a]:
                ans += 1

print(ans)