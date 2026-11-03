#100点解法
N = int(input())
a = list(map(int, input().split()))

ans = 0
l = 0
r = 0
while l < N:
    while r < l or (r+1 < N and a[r+1] > a[r]):
        r += 1
    ans += r - l + 1
    l += 1

print(ans)