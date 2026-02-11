from collections import deque

N = int(input())

T = [0] * N
K = [0] * N
A = [[] for _ in range(N)]
for i in range(N):
    T[i], K[i], *A[i] = map(int, input().split())

ans = 0
acquired = [False] * N
q = deque([N])
while q:
    v = q.popleft()
    ans += T[v-1]
    for u in A[v-1]:
        if not acquired[u-1]:
            acquired[u-1] = True
            q.append(u)

print(ans)