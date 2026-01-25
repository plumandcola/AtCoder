import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(map(int, input().split()))

ans = float("inf")
for i in range(N):
    j = bisect.bisect_left(B, A[i])
    if j != 0:
        ans = min(ans, A[i] - B[j-1])
    if j != M:
        ans = min(ans, B[j] - A[i])

print(ans)