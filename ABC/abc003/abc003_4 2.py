def c(n: int, r: int) -> int:
    r = min(r, n-r)
    if r < 0:
        return 0
    
    ans = 1
    for i in range(n-r+1, n+1):
        ans *= i
    for i in range(2, r+1):
        ans //= i
    return ans % mod


R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())
mod = 1000000007

dp = [[c(x*y, D) * c(x*y - D, L) for y in range(Y+1)] for x in range(X+1)]
"""dp[x][y] := ちょうどx行y列の区画に、D個のデスクトップとL個のサーバーラックを配置するパターン数"""
for x in range(1, X+1):
    for y in range(1, Y+1):
        for i in range(1, x+1):
            for j in range(1, y+1):
                if i != x or j != y:
                    dp[x][y] = (dp[x][y] - dp[i][j] * (x-i+1) * (y-j+1)) % mod

print(dp[X][Y] * (R-X+1) * (C-Y+1) % mod)