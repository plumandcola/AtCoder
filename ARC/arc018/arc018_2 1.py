N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            s = (x[j] - x[i]) * (y[k] - y[i]) - (x[k] - x[i]) * (y[j] - y[i])
            if s % 2 == 0 and s != 0:
                ans += 1

print(ans)