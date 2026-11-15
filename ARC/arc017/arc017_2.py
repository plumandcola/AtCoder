N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
l = 0
r = 1
while l < N:
    while r < N and A[r] > A[r-1]:
        r += 1
    
    ans += max(0, r - l - K + 1)
    l = r
    r = l + 1

print(ans)