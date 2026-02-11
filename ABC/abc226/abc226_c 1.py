import sys

sys.setrecursionlimit(1000000)

def dfs(v: int) -> int:
    ans = 0
    for u in A[v-1]:
        if not acquired[u-1]:
            acquired[u-1] = True
            ans += dfs(u)
    ans += T[v-1]
    return ans


N = int(input())

T = [0] * N
K = [0] * N
A = [[] for _ in range(N)]
for i in range(N):
    T[i], K[i], *A[i] = map(int, input().split())

acquired = [False] * N
print(dfs(N))