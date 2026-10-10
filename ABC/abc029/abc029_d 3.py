#100点解法
N = input()
n = len(N)

dp = [[[0] * (n+1) for b in range(2)] for i in range(n+1)]
"""dp[i][b][j], j: 1が何個含まれているか"""
dp[0][0][0] = 1
for i in range(n):
    for b in range(2):
        limit = 9 if b == 1 else int(N[i])
        for j in range(n):
            for d in range(limit + 1):
                B = b | (d < int(N[i]))
                J = j + (d == 1)
                dp[i+1][B][J] += dp[i][b][j]

ans = 0
for j in range(n+1):
    ans += (dp[n][0][j] + dp[n][1][j]) * j

print(ans)