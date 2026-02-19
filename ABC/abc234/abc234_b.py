N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        ans = max(ans, dx * dx + dy * dy)

print(ans ** 0.5)