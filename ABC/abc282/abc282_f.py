import bisect

N = int(input())

lr = []
for l in range(1, N+1):
    i = 1
    while l + i - 1 <= N:
        lr.append((l, l + i - 1))
        i *= 2

print(len(lr))
for l, r in lr:
    print(l, r)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    i = 1
    while 2 * i <= R - L + 1:
        i *= 2
    
    a = bisect.bisect_left(lr, (L, L+i-1))
    b = bisect.bisect_left(lr, (R-i+1, R))
    print(a+1, b+1)
