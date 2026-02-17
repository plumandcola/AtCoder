import itertools

N, M = map(int, input().split())

g1 = [[0]*N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g1[A-1][B-1] = 1
    g1[B-1][A-1] = 1

g2 = [[0]*N for _ in range(N)]
for _ in range(M):
    C, D = map(int, input().split())
    g2[C-1][D-1] = 1
    g2[D-1][C-1] = 1

for p in itertools.permutations(range(N)):
    same = True
    for i in range(N):
        for j in range(N):
            if g1[i][j] != g2[p[i]][p[j]]:
                same = False
    if same == True:
        print("Yes")
        break
else:
    print("No")