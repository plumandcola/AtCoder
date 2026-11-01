N, X = map(int, input().split())

coins = []
for i in range(N):
    A, B = map(int, input().split())
    k = 1
    while k < B:
        coins.append(A * k)
        B -= k
        k <<= 1
    if B > 0:
        coins.append(A * B)

dp = [False] * (X+1)
dp[0] = True
for A in coins:
    for i in range(X-A, -1, -1):
        dp[i+A] |= dp[i]

print("Yes" if dp[X] else "No")