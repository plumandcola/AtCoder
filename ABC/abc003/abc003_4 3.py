c = {} #(n, r) -> nCr

def calc_c(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    
    if r == 0 or r == n:
        return 1
    
    if (n, r) not in c:
        c[(n, r)] = (calc_c(n-1, r-1) + calc_c(n-1, r)) % mod
    
    return c[(n, r)]


R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())
mod = 1000000007

dp = [[calc_c(x*y, D) * calc_c(x*y - D, L) for y in range(Y+1)] for x in range(X+1)]
"""dp[x][y] := ちょうどx行y列の区画に、D個のデスクトップとL個のサーバーラックを配置するパターン数"""
for x in range(1, X+1):
    for y in range(1, Y+1):
        for i in range(1, x+1):
            for j in range(1, y+1):
                if i != x or j != y:
                    dp[x][y] = (dp[x][y] - dp[i][j] * (x-i+1) * (y-j+1)) % mod

print(dp[X][Y] * (R-X+1) * (C-Y+1) % mod)