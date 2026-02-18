from collections import defaultdict

N, X = map(int, input().split())

L = [0] * N
a = [[] for _ in range(N)]
for i in range(N):
    L[i], *a[i] = map(int, input().split())

dp = [defaultdict(int) for _ in range(N+1)]
dp[0][1] = 1
for i in range(N):
    for p in dp[i]:
        for j in range(L[i]):
            P = p * a[i][j]
            if P <= X:
                dp[i+1][P] += dp[i][p]

print(dp[N][X])