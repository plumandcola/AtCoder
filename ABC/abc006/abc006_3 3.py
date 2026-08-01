N, M = map(int, input().split())

y = M % 2

if y == 1:
    N -= 1
    M -= 3

x = 2 * N - M // 2
z = - N + M // 2

if x < 0 or z < 0:
    print(-1, -1, -1)
else:
    print(x, y, z)