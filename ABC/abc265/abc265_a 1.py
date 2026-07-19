X, Y, N = map(int, input().split())

print((N // 3) * min(3*X, Y) + (N % 3) * X)