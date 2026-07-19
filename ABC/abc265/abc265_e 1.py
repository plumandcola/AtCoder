N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
obstacles = set(tuple(map(int, input().split())) for _ in range(M))
mod = 998244353

ans = 0
dp = [[[0] * (N+1) for j in range(N+1)] for i in range(N+1)]
dp[0][0][0] = 1
for i in range(N+1):
    for j in range(N-i+1):
        for k in range(N-i-j+1):
            if (A*i + C*j + E*k, B*i + D*j + F*k) in obstacles:
                dp[i][j][k] = 0
                continue
            
            dp[i][j][k] %= mod

            if i+j+k == N:
                ans = (ans + dp[i][j][k]) % mod
                continue

            dp[i+1][j][k] += dp[i][j][k]
            dp[i][j+1][k] += dp[i][j][k]
            dp[i][j][k+1] += dp[i][j][k]

print(ans)