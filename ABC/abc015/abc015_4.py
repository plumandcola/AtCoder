W = int(input())
N, K = map(int, input().split())

dp = [[0] * (W+1) for _ in range(K+1)]
"""dp[i][j] := i枚のスクリーンショットを貼りつけてjの幅を使った時の、重要度の合計の最大値"""
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(K-1, -1, -1):
        for j in range(W-A, -1, -1):
            dp[i+1][j+A] = max(dp[i+1][j+A], dp[i][j] + B)

print(max(max(dp[i]) for i in range(K+1)))