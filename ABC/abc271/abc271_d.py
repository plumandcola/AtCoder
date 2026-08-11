N, S = map(int, input().split())

a = [0] * N
b = [0] * N
dp = [[False] * (S+1) for _ in range(N+1)]
"""dp[i][s] := i枚目のカードまでを使って、和をsにできるかどうか"""
dp[0][0] = True

for i in range(N):
    a[i], b[i] = map(int, input().split())
    for j in range(S, -1, -1):
        if j + a[i] <= S:
            dp[i+1][j + a[i]] |= dp[i][j]
        if j + b[i] <= S:
            dp[i+1][j + b[i]] |= dp[i][j]

print("Yes" if dp[N][S] else "No")

if dp[N][S]:
    ans = [""] * N
    for i in range(N-1, -1, -1):
        if S - a[i] >= 0 and dp[i][S - a[i]]:
            ans[i] = "H"
            S -= a[i]
        elif S - b[i] >= 0 and dp[i][S - b[i]]:
            ans[i] = "T"
            S -= b[i]
    print(*ans, sep="")
