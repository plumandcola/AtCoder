N, M, K, S, T, X = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    g[U-1].append(V-1)
    g[V-1].append(U-1)

dp = [[[0] * N for _ in range(2)] for _ in range(K+1)]
"""
dp[i][b][v]
i: Aの長さ
b: 0ならXが偶数回、1ならXが奇数回
v: Aの末尾
"""
dp[0][0][S-1] = 1
for i in range(K):
    for b in range(2):
        for v in range(N):
            if v == X-1:
                dp[i+1][b][v] = sum(dp[i][b^1][u] for u in g[v]) % 998244353
            else:
                dp[i+1][b][v] = sum(dp[i][b][u] for u in g[v]) % 998244353

print(dp[K][0][T-1])