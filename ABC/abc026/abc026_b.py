import math

N = int(input())
R = sorted([int(input()) for _ in range(N)], reverse=True)

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += R[i] ** 2
    else:
        ans -= R[i] ** 2

print(ans * math.pi)