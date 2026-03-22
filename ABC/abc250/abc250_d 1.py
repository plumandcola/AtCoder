import bisect

N = int(input())

#二分探索で、Nの3乗根(切り上げ)を求める
l = 0
r = 10**6 + 1
while l != r:
    mid = (l+r) // 2
    if mid ** 3 < N:
        l = mid + 1
    else:
        r = mid

N_cbrt = l #Nの3乗根(切り上げ)

is_prime = [True] * (N_cbrt+1)
is_prime[0] = False #0は素数じゃない
is_prime[1] = False #1は素数じゃない
primes = []
for n in range(2, N_cbrt+1):
    if is_prime[n]: #nが素数なら
        primes.append(n)
        for i in range(2*n, N_cbrt+1, n):
            is_prime[i] = False

ans = 0
for q in primes:
    ans += bisect.bisect_left(primes, min(q, N // (q**3) + 1))

print(ans)