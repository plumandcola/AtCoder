N = int(input())

g = 0
for i in range(N):
    X, Y, Z = map(int, input().split())
    x_M = 0
    x_m = X - 1
    y_M = 0
    y_m = Y - 1
    z_M = 0
    z_m = Z - 1

    M = int(input())
    for j in range(M):
        x, y, z = map(int, input().split())
        x_M = max(x_M, x)
        x_m = min(x_m, x)
        y_M = max(y_M, y)
        y_m = min(y_m, y)
        z_M = max(z_M, z)
        z_m = min(z_m, z)

    g ^= X - 1 - x_M
    g ^= x_m
    g ^= Y - 1 - y_M
    g ^= y_m
    g ^= Z - 1 - z_M
    g ^= z_m

print("WIN" if g != 0 else "LOSE")