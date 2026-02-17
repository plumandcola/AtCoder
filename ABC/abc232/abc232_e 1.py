H, W, K = map(int, input().split())
x_1, y_1, x_2, y_2 = map(int, input().split())

dp = [[0] * 4 for _ in range(K+1)]
"""
dp[i][b] := i回目の操作の後、
b=0 -> x != x_2 and y != y_2
b=1 -> x == x_2 abd y != y_2
b=2 -> x != x_2 and y == y_2
b=3 -> x == x_2 and y == y_2
となる場合の数
"""
b = int(x_1 == x_2) | (int(y_1 == y_2) << 1)
dp[0][b] = 1

for i in range(K):
    dp[i+1][0] = ((H+W-4) * dp[i][0] + (H-1) * dp[i][1] + (W-1) * dp[i][2]) % 998244353
    dp[i+1][1] = (dp[i][0] + (W-2) * dp[i][1] + (W-1) * dp[i][3]) % 998244353
    dp[i+1][2] = (dp[i][0] + (H-2) * dp[i][2] + (H-1) * dp[i][3]) % 998244353
    dp[i+1][3] = (dp[i][1] + dp[i][2]) % 998244353

print(dp[K][3])