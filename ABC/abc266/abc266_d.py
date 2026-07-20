N = int(input())

dp = [[0] * 5 for _ in range(100001)]
for i in range(1, 5):
    dp[0][i] = -float("inf")

for _ in range(N):
    T, X, A = map(int, input().split())
    dp[T][X] += A

for T in range(100000):
    for X in range(5):
        l = max(0, X-1)
        r = min(4, X+1) + 1
        dp[T+1][X] += max(dp[T][l:r])

print(max(dp[100000]))