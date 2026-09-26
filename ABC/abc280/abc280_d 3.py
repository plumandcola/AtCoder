import math

K = int(input())

for i in range(1, 2000001):
    K //= math.gcd(K, i)
    if K == 1:
        print(i)
        break
else:
    print(K)
