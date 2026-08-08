X, Y, Z = map(int, input().split())

if X < 0:
    X *= -1
    Y *= -1
    Z *= -1

if Y < 0 or X < Y:
    print(X)
elif 0 < Z < Y:
    print(X)
elif Z < 0:
    print(X - 2 * Z)
else:
    print(-1)
