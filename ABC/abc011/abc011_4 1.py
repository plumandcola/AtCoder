#90点解法
import sys
sys.setrecursionlimit(10000000)

def dfs(i: int, x: int, X: int, y: int, Y: int, D: int) -> int:
    if i == 0:
        if x == X and y == Y: return 1
        else: return 0

    ans = 0
    ans += dfs(i-1, x+D, X, y, Y, D)
    ans += dfs(i-1, x-D, X, y, Y, D)
    ans += dfs(i-1, x, X, y+D, Y, D)
    ans += dfs(i-1, x, X, y-D, Y, D)
    return ans


N, D = map(int, input().split())
X, Y = map(int, input().split())

print(dfs(N, 0, X, 0, Y, D) / pow(4, N))