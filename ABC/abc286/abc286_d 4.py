N, X = map(int, input().split())

mask = (1 << (X+1)) - 1

dp = 1
for i in range(N):
    A, B = map(int, input().split())
    for j in range(1, B+1):
        dp |= dp << A
        dp &= mask

print("Yes" if (dp >> X) & 1 else "No")