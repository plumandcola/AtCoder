#100点解法
def c(n: int, r: int) -> int:
    ans = 1
    for i in range(n-r+1, n+1):
        ans *= i
    for i in range(2, r+1):
        ans //= i
    return ans


R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

print(c(X*Y, D) * (R-X+1) * (C-Y+1) % 1000000007)