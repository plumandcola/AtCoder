import sys

sys.setrecursionlimit(1000000)

def dfs(p: int, i: int) -> int:
    if i == N:
        return int(p == X)
    
    result = 0
    for j in range(L[i]):
        result += dfs(p * a[i][j], i + 1)
    
    return result


N, X = map(int, input().split())

L = [0] * N
a = [[] for _ in range(N)]
for i in range(N):
    L[i], *a[i] = map(int, input().split())

print(dfs(1, 0))