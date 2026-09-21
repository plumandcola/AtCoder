H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

count = [[[0] * N for j in range(W+1)] for i in range(H+1)]
for i in range(H):
    for j in range(W):
        for n in range(N):
            count[i+1][j+1][n] = count[i+1][j][n] + count[i][j+1][n] - count[i][j][n] + (A[i][j] == n+1)

ans = [[0] * (W-w+1) for _ in range(H-h+1)]
for i in range(H-h+1):
    for j in range(W-w+1):
        for n in range(N):
            if count[H][W][n] - count[i+h][j+w][n] + count[i+h][j][n] + count[i][j+w][n] - count[i][j][n] > 0:
                ans[i][j] += 1

for i in range(H-h+1):
    print(*ans[i])
