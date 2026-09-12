import math

N = int(input())
a = list(map(int, input().split()))

g = math.gcd(*a)

ans = 0
for i in range(N):
    m = a[i] // g
    while m % 2 == 0:
        ans += 1
        m //= 2
    while m % 3 == 0:
        ans += 1
        m //= 3
    
    if m != 1:
        ans = -1
        break

print(ans)