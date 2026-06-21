N, M = map(int, input().split())
X = list(map(int, input().split()))

bonus = [0] * (N+1)
for _ in range(M):
    C, Y = map(int, input().split())
    bonus[C] = Y

dp = [[-float("inf")] * (N+1) for _ in range(N+1)]
"""dp[i][j] := コイントスをi回行ってカウンタの数値がjのときに、高橋君が最大で何円もらうことができるか"""
dp[0][0] = 0

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + bonus[j+1]) #表が出たとき
        dp[i+1][0] = max(dp[i+1][0], dp[i][j]) #裏が出たとき

print(max(dp[N]))