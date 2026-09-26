from collections import defaultdict

K = int(input())

prime_factors = defaultdict(int)
n = K
i = 2
while i * i <= K:
    while n%i == 0:
        prime_factors[i] += 1
        n //= i
    i += 1
if n != 1:
    prime_factors[n] += 1

#二分探索
l = -1
r = K + 1
while r - l > 1:
    mid = (l + r) // 2
    for p in prime_factors: #midの階乗がpで何回割れるかを調べる
        count = 0 #midの階乗がpで何回割れるか
        n = mid
        while n:
            count += n // p
            n //= p
        if count < prime_factors[p]: #midの階乗がKの倍数よりも、素因数pが少ない
            l = mid
            break
    else: #全てのpについて素因数pの個数が、midの階乗がKの倍数以上
        r = mid

print(r)