from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]

q = deque()
q.append((sy-1, sx-1))
d = [[-1] * C for _ in range(R)]
d[sy-1][sx-1] = 0

while q:
    y, x = q.popleft()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if c[y + dy][x + dx] == "." and d[y + dy][x + dx] == -1:
            d[y + dy][x + dx] = d[y][x] + 1
            q.append((y + dy, x + dx))

print(d[gy-1][gx-1])