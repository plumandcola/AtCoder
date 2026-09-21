H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

up = [0] * (H+1) #up[i] := i行目から上に現れる数の集合
for i in range(H):
    up[i+1] = up[i]
    for j in range(W):
        up[i+1] |= 1 << A[i][j]

down = [0] * (H+1) #down[i] := i行目から下に現れる数の集合
for i in range(H-1, -1, -1):
    down[i] = down[i+1]
    for j in range(W):
        down[i] |= 1 << A[i][j]

left = [0] * (W+1) #left[j] := j列目から左に現れる数の集合
for j in range(W):
    left[j+1] = left[j]
    for i in range(H):
        left[j+1] |= 1 << A[i][j]

right = [0] * (W+1) #right[j] := j列目から右に現れる数の集合
for j in range(W-1, -1, -1):
    right[j] = right[j+1]
    for i in range(H):
        right[j] |= 1 << A[i][j]

for i in range(H-h+1):
    ans = [0] * (W-w+1)
    for j in range(W-w+1):
        b = up[i] | down[i+h] | left[j] | right[j+w]
        ans[j] = b.bit_count()
    print(*ans)
