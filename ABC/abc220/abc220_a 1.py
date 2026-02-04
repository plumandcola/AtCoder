A, B, C = map(int, input().split())

Y = B // C * C

if Y >= A:
    print(Y)
else:
    print(-1)