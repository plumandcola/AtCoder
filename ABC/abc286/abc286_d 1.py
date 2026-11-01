N, X = map(int, input().split())

dp = [False] * (X+1)
dp[0] = True
for i in range(N):
    A, B = map(int, input().split())
    for j in range(B):
        for k in range(X-A, -1, -1):
            dp[k+A] |= dp[k]

print("Yes" if dp[X] else "No")