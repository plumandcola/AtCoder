#50点解法
def dfs(W: int, H: int) -> int:
    if W == 1 and H == 1:
        return 1
    
    ans = 0
    if W > 1:
        ans += dfs(W-1, H)
    if H > 1:
        ans += dfs(W, H-1)
    return ans % mod


W, H = map(int, input().split())
mod = 1000000007

if W <= 10 and H <= 10:
    print(dfs(W, H))
