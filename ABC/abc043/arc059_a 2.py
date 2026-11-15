N = int(input())
a = list(map(int, input().split()))

s = sum(a)
ss = sum(a[i] ** 2 for i in range(N))

print(min(ss - 2 * s * x + N * x * x for x in range(-100, 101)))