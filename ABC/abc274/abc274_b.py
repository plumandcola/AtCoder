H, W = map(int, input().split())
C = [input() for _ in range(H)]

print(*(sum(C[i][j] == '#' for i in range(H)) for j in range(W)))