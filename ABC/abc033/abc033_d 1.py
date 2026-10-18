#30点解法
N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

ans = [0] * 3
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            inner_products = [0] * 3
            inner_products[0] = (x[j] - x[i]) * (x[k] - x[i]) + (y[j] - y[i]) * (y[k] - y[i])
            inner_products[1] = (x[i] - x[j]) * (x[k] - x[j]) + (y[i] - y[j]) * (y[k] - y[j])
            inner_products[2] = (x[i] - x[k]) * (x[j] - x[k]) + (y[i] - y[k]) * (y[j] - y[k])
            if any(inner_products[i] < 0 for i in range(3)):
                ans[2] += 1
            elif any(inner_products[i] == 0 for i in range(3)):
                ans[1] += 1
            else:
                ans[0] += 1

print(*ans)