#300点解法
from collections import defaultdict

N, A = map(int, input().split())
x = list(map(int, input().split()))

dp = [defaultdict(int) for _ in range(N+1)] #dp[i][s] := i番目までのカードを使って、x - Aの和がsになる場合の数
dp[0][0] = 1
for i in range(N):
    for s in dp[i]:
        dp[i+1][s] += dp[i][s]
        dp[i+1][s + x[i] - A] += dp[i][s]

print(dp[N][0] - 1) #0枚の場合を引く