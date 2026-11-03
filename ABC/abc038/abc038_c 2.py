#100点解法
N = int(input())
a = list(map(int, input().split()))

ans = 0
l = 0
r = 1
while l < N:
    while r < N and a[r] > a[r-1]:
        r += 1
    ans += (r - l) * (r - l + 1) // 2
    l = r
    r += 1

print(ans)