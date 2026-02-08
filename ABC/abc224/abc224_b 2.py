H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = True
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] + A[i+1][j+1] > A[i+1][j] + A[i][j+1]:
            ans = False

print("Yes" if ans else "No")