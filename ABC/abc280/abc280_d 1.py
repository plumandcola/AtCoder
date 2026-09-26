K = int(input())

ans = 1
p = 2
while p * p <= K:
    a = 0 #Kをpで何回割り切れるか
    while K % p == 0:
        K //= p
        a += 1

    n = 0 #n!がp^aの倍数となる最小のn
    while a > 0:
        n += p
        x = n
        while x % p == 0:
            x //= p
            a -= 1

    ans = max(ans, n)

    p += 1

ans = max(ans, K)

print(ans)