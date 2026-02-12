N = int(input())

ans = 0
A = 1
while A * A * A <= N:
    B = A
    while A * B * B <= N:
        ans += N // (A*B) - B + 1
        B += 1
    A += 1

print(ans)