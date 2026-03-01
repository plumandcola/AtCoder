N = int(input())

dp = [[0] * 9 for _ in range(N)]
for j in range(9):
    dp[0][j] = 1

for i in range(N-1):
    for j in range(9):
        if j > 0:
            dp[i+1][j] += dp[i][j-1]
        
        dp[i+1][j] += dp[i][j]

        if j < 8:
            dp[i+1][j] += dp[i][j+1]
        
        dp[i+1][j] %= 998244353

print(sum(dp[N-1]) % 998244353)