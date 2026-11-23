import math

T = int(input())
for _ in range(T):
    N, D, K = map(int, input().split())
    K -= 1
    g = math.gcd(N, D)
    cycle = N // g
    print((K // cycle + D * K) % N)
