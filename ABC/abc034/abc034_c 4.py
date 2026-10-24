#100点解法
def c(n, r):
    r = min(r, n-r)
    ans = 1
    for i in range(n-r+1, n+1):
        ans *= i
    for i in range(2, r+1):
        ans //= i
    return ans % mod


W, H = map(int, input().split())
mod = 1000000007

print(c(W+H-2, W-1))