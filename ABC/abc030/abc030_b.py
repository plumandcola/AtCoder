n, m = map(int, input().split())

if n > 12:
    n -= 12

degree = abs((30*n + m/2) - (6*m))

print(min(degree, 360 - degree))