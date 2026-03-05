def f(a: int, b: int) -> int:
    return a*a*a + a*a*b + a*b*b + b*b*b


N = int(input())

ans = float("inf")
a = 0
while 4*a*a*a <= 10 ** 18:
    l = a
    r = 1000001
    while l != r:
        mid = (l+r) // 2
        if f(a, mid) < N:
            l = mid + 1
        else:
            r = mid
    ans = min(ans, f(a, l))
    a += 1

print(ans)