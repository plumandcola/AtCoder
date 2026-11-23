#300点解法
N, A = map(int, input().split())
x = list(map(int, input().split()))

dp = [[0] * (50 * N + 1) for _ in range(N+1)] #dp[j][s] := j枚のカードを使って和がsになる場合の数
dp[0][0] = 1
for i in range(N):
    for j in range(N-1, -1, -1):
        for s in range(50 * N - x[i] + 1):
            dp[j+1][s + x[i]] += dp[j][s]

print(sum(dp[i][i * A] for i in range(1, N+1)))