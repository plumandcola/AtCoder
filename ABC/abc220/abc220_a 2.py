A, B, C = map(int, input().split())

if B // C - (A-1) // C == 0:
    print(-1)
else:
    print(B // C * C)