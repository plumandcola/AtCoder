p_max = 2100000
primes = []
is_prime = [True] * (p_max + 1)
is_prime[0] = False
is_prime[1] = False
for p in range(2, p_max + 1):
    if is_prime[p] == True:
        primes.append(p)
        for n in range(p*p, p_max + 1, p):
            is_prime[n] = False

T = int(input())
for _ in range(T):
    N = int(input())
    for p in primes:
        if N % p == 0:
            if N % (p*p) == 0:
                print(p, N//p//p)
                break
            else:
                m = N // p
                #二分探索
                l = 0
                r = m
                while r - l > 1:
                    mid = (l + r) // 2
                    if mid * mid > m:
                        r = mid
                    else:
                        l = mid
                print(l, p)
                break
