N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

i0 = (B[0][0] - 1) // 7
j0 = (B[0][0] - 1) % 7

ans = True
for i in range(N):
    for j in range(M):
        if B[i][j] != (i + i0) * 7 + (j + j0) % 7 + 1:
            ans = False

print("Yes" if ans else "No")