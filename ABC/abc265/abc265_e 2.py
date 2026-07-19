from collections import defaultdict

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
obstacles = set(tuple(map(int, input().split())) for _ in range(M))
mod = 998244353

ans = [defaultdict(int) for _ in range(N+2)] #ans[i][(x, y)] := i回ワープをして(x, y)に移動する経路の数
ans[0][(0, 0)] = 1
for i in range(N+1):
    for x, y in ans[i]:
        if (x, y) in obstacles:
            ans[i][(x, y)] = 0
            continue

        ans[i][(x, y)] %= mod
        
        ans[i+1][(x+A, y+B)] += ans[i][(x, y)]
        ans[i+1][(x+C, y+D)] += ans[i][(x, y)]
        ans[i+1][(x+E, y+F)] += ans[i][(x, y)]

print(sum(ans[N].values()) % mod)