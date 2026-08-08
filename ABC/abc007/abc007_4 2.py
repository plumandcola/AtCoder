#100点解法
def count(N: int) -> int:
    """N以下の数字のうち、4か9が含まれている数字の個数"""
    N = str(N)
    n = len(N)
    dp = [[[0] * 2 for _ in range(2)] for _ in range(n+1)]
    """dp[i][b1][b2], b2: 4か9が含まれているかどうか"""
    dp[0][0][0] = 1

    for i in range(n):
        for b1 in range(2):
            limit = 9 if b1 == 1 else int(N[i])
            for b2 in range(2):
                for d in range(limit + 1):
                    B1 = b1 | (d < int(N[i]))
                    B2 = b2 | (d == 4) | (d == 9)
                    dp[i+1][B1][B2] += dp[i][b1][b2]
    
    return dp[n][0][1] + dp[n][1][1]


A, B = map(int, input().split())

print(count(B) - count(A-1))