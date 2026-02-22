H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for j in range(W):
    print(*[A[i][j] for i in range(H)])