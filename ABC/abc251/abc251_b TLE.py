N, W = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (W+1) for _ in range(4)]
"""dp[i][w] := i個以下の異なるおもりを選んで、選んだおもりの重さの和をwにすることができるかどうか"""
for i in range(4):
    dp[i][0] = True

for a in A:
    for i in range(2, -1, -1):
        for w in range(W+1):
            dp[i+1][w] |= dp[i][w]

            if w+a <= W:
                dp[i+1][w+a] |= dp[i][w]

print(sum(dp[3][1:]))