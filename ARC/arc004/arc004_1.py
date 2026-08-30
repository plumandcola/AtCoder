N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(1, N):
    for j in range(i):
        ans = max(ans, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

print(ans ** 0.5)