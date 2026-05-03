N = int(input())

least_prime_factors = list(range(N+1)) #最小素因数
for p in range(2, N+1):
    for i in range(2 * p, N+1, p):
        least_prime_factors[i] = min(least_prime_factors[i], p)

ans = 0
for i in range(1, N+1):
    m = 1 #平方数にするために掛けなければいけない最小の数
    while i != 1:
        j = least_prime_factors[i]
        while i % (j * j) == 0:
            i //= j * j
        if i % j == 0: #iを素因数jで割れる回数が奇数回
            m *= j
            i //= j
    
    ans += int((N // m) ** 0.5)
    
print(ans)