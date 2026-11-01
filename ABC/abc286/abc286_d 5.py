N, X = map(int, input().split())

mask = (1 << (X+1)) - 1

dp = 1
for i in range(N):
    A, B = map(int, input().split())
    k = 1
    while k < B:
        dp |= dp << (A * k)
        dp &= mask
        B -= k
        k <<= 1
    if B > 0:
        dp |= dp << (A * B)
        dp &= mask

print("Yes" if (dp >> X) & 1 else "No")