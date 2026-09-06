from collections import deque

H, W = map(int, input().split())
c = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if c[i][j] == 's':
            sx = i
            sy = j
        elif c[i][j] == 'g':
            gx = i
            gy = j

d = [[-1] * W for _ in range(H)]
d[sx][sy] = 0
q = deque([(sx, sy)])
while q:
    i, j = q.popleft()
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= i + di < H and 0 <= j + dj < W and d[i + di][j + dj] == -1:
            if c[i + di][j + dj] != '#':
                d[i + di][j + dj] = d[i][j]
                q.appendleft((i + di, j + dj))
            else:
                d[i + di][j + dj] = d[i][j] + 1
                q.append((i + di, j + dj))

print("YES" if 0 <= d[gx][gy] <= 2 else "NO")