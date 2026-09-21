N = int(input())

spf = list(range(N+1)) #spf = smallest prime factor = 最小素因数
for p in range(2, N+1):
    for i in range(p * p, N+1, p):
        spf[i] = min(spf[i], p)

ans = 0
for i in range(1, N+1):
    m = 1 #平方数にするために掛けなければいけない最小の数
    while i != 1:
        j = spf[i]
        while i % (j * j) == 0:
            i //= j * j
        if i % j == 0: #iを素因数jで割れる回数が奇数回
            m *= j
            i //= j
    
    ans += int((N // m) ** 0.5)
    
print(ans)
