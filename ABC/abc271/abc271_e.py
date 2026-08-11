N, M, K = map(int, input().split())

A = [0] * M
B = [0] * M
C = [0] * M
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())

ans = [float("inf")] * N
ans[0] = 0
for E in map(int, input().split()):
    E -= 1
    a = A[E] - 1
    b = B[E] - 1
    c = C[E]
    ans[b] = min(ans[b], ans[a] + c)

print(ans[N-1] if ans[N-1] != float("inf") else -1)