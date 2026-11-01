def f(i: int, j: int) -> int:
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        ans = 1
        if i-1 >= 0 and a[i-1][j] < a[i][j]: ans += f(i-1, j)
        if i+1 < H and a[i+1][j] < a[i][j]: ans += f(i+1, j)
        if j-1 >= 0 and a[i][j-1] < a[i][j]: ans += f(i, j-1)
        if j+1 < W and a[i][j+1] < a[i][j]: ans += f(i, j+1)

        ans %= mod
        dp[i][j] = ans
        return ans


H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
mod = 1000000007

dp = [[-1] * W for _ in range(H)]

print(sum(sum(f(i, j) for j in range(W)) for i in range(H)) % mod)