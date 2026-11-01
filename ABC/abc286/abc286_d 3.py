N, X = map(int, input().split())

dp = [False] * (X+1)
dp[0] = True
for i in range(N):
    A, B = map(int, input().split())
    mx = [-float("inf")] * A #mx[j] := j' = j, j-A, j-2A, ...のうちdp[j']がTrueであるような最大のj'(存在しなければ-∞)
    for j in range(X+1):
        if dp[j]:
            mx[j % A] = j

        if mx[j % A] >= j - A*B:
            dp[j] = True
        else:
            dp[j] = False

print("Yes" if dp[X] else "No")