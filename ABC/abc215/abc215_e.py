N = int(input())
S = input()

dp = [[[0] * 10 for b in range(1 << 10)] for i in range(N+1)]
"""
dp[i][b][j] := i回目のコンテストまでで、
ビット列bで表される集合Sに含まれる種類のコンテストに出場し、
最後に出場したコンテストがj種類目である選び方の総数
"""
dp[0][0][0] = 1
for i in range(N):
    n = ord(S[i]) - ord('A')
    for b in range(1 << 10):
        for j in range(10):
            dp[i+1][b][j] = (dp[i+1][b][j] + dp[i][b][j]) % 998244353 #参加しない
            if b >> n & 1 == 0 or j == n: #参加する条件を満たしている時
                dp[i+1][b | (1 << n)][n] = (dp[i+1][b | (1 << n)][n] + dp[i][b][j]) % 998244353 #参加する

ans = 0
for b in range(1 << 10):
    for j in range(10):
        ans = (ans + dp[N][b][j]) % 998244353

print((ans - 1) % 998244353)