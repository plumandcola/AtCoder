from collections import defaultdict

N = int(input())

ans = 0
for i in range(1, N+1):
    prime_factors = defaultdict(int)
    for j in range(2, int(N**0.5) + 1):
        while i % j == 0:
            prime_factors[j] += 1
            i //= j
    if i != 1:
        prime_factors[i] += 1
    
    m = 1 #平方数にするために掛けなければいけない最小の数
    for p in prime_factors:
        if prime_factors[p] % 2 == 1:
            m *= p
    
    ans += int((N // m) ** 0.5)

print(ans)