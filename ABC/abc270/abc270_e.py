N, K = map(int, input().split())
A = list(map(int, input().split()))

#かご1つから食べられるりんごの個数を二分探索
l = 0
r = K
while r - l > 1:
    mid = (l + r) // 2
    s = sum(min(A[i], mid) for i in range(N))
    if s > K:
        r = mid
    else:
        l = mid

ans = [0] * N
s = 0
for i in range(N):
    ans[i] = max(0, A[i] - l)
    s += A[i] - ans[i]

for i in range(N):
    if ans[i] > 0 and s < K:
        ans[i] -= 1
        s += 1

print(*ans)