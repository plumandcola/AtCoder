import math

N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

spells = set()
for i in range(N-1):
    for j in range(i+1, N):
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        g = math.gcd(dx, dy)
        spells.add(((dx) // g, (dy) // g))
        spells.add((- (dx) // g, - (dy) // g))

print(len(spells))