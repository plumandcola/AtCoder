H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

min_X = [H] * (N+1)
max_X = [-1] * (N+1)
min_Y = [W] * (N+1)
max_Y = [-1] * (N+1)

for i in range(H):
    for j in range(W):
        min_X[A[i][j]] = min(min_X[A[i][j]], i)
        max_X[A[i][j]] = max(max_X[A[i][j]], i)
        min_Y[A[i][j]] = min(min_Y[A[i][j]], j)
        max_Y[A[i][j]] = max(max_Y[A[i][j]], j)

ans = [[N] * (W-w+1) for _ in range(H-h+1)]
for i in range(H-h+1):
    for j in range(W-w+1):
        for n in range(1, N+1):
            if i <= min_X[n] and max_X[n] < i+h and j <= min_Y[n] and max_Y[n] < j+w:
                ans[i][j] -= 1

for i in range(H-h+1):
    print(*ans[i])
