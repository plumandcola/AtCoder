#50点解法
N = int(input())

Ax = [0] * N
Ay = [0] * N
for i in range(N):
    Ax[i], Ay[i] = map(int, input().split())

Bx = [0] * N
By = [0] * N
for i in range(N):
    Bx[i], By[i] = map(int, input().split())

s1 = 0
for i in range(N-1):
    for j in range(i+1, N):
        s1 += (Ax[i] - Ax[j]) ** 2 + (Ay[i] - Ay[j]) ** 2

s2 = 0
for i in range(N-1):
    for j in range(i+1, N):
        s2 += (Bx[i] - Bx[j]) ** 2 + (By[i] - By[j]) ** 2

print((s2 / s1) ** 0.5)