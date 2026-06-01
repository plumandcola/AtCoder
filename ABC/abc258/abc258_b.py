N = int(input())
A = [list(map(int, input())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for di, dj in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
            ans_ij = 0
            for t in range(N):
                ans_ij = ans_ij * 10 + A[i][j]
                i = (i + di + N) % N
                j = (j + dj + N) % N
            ans = max(ans, ans_ij)

print(ans)