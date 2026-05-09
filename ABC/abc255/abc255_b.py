N, K = map(int, input().split())
A = list(map(int, input().split()))

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 0
for i in range(N):
    ans_i = float("inf")
    for j in range(K):
        x_i = X[i]
        y_i = Y[i]
        x_j = X[A[j] - 1]
        y_j = Y[A[j] - 1]
        ans_i = min(ans_i, (x_i - x_j) ** 2 + (y_i - y_j) ** 2)
    ans = max(ans, ans_i)

print(ans ** 0.5)