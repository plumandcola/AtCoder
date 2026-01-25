N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted([(a, 0) for a in A] + [(b, 1) for b in B])
ans = float("inf")
for i in range(N+M-1):
    if C[i][1] != C[i+1][1]:
        ans = min(ans, C[i+1][0] - C[i][0])

print(ans)