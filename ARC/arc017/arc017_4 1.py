#0点解法
import math

N = int(input())
a = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    t, l, r = map(int, input().split())
    if t == 0:
        print(math.gcd(*a[l-1 : r]))
    else:
        for i in range(l-1, r):
            a[i] += t
