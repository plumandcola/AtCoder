import sys
sys.setrecursionlimit(10000000)

N = int(input())
mod = 1000000007

g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

dp_w = [1] * N
"""dp_w[v] := 島vが白で塗られる、色の塗り方"""
dp_b = [1] * N
"""dp_b[v] := 島vが黒で塗られる、色の塗り方"""

def dfs(v: int, p: int):
    for u in g[v]:
        if u == p: continue

        dfs(u, v)
        dp_w[v] = dp_w[v] * (dp_w[u] + dp_b[u]) % mod
        dp_b[v] = dp_b[v] * dp_w[u] % mod

dfs(0, -1)

print((dp_w[0] + dp_b[0]) % mod)