def f(a: int, b: int) -> int:
    return a*a*a + a*a*b + a*b*b + b*b*b


N = int(input())

ans = float("inf")
a = 0
while 4*a*a*a < ans:
    l = a - 1
    r = 1000001
    while r - l > 1:
        mid = (l + r) // 2
        if f(a, mid) < N:
            l = mid
        else:
            r = mid
    ans = min(ans, f(a, r))
    a += 1

print(ans)
