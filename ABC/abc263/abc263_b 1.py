N = int(input())
P = list(map(int, input().split()))

dp = [0] * N
for i in range(1, N):
    dp[i] = dp[P[i-1] - 1] + 1

print(dp[N-1])