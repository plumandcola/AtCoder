import bisect
from collections import defaultdict, deque

H, W, N = map(int, input().split())
s_x, s_y = map(int, input().split())
g_x, g_y = map(int, input().split())

obstacles_row = defaultdict(list) #obstacles_row[X] := 上からX行目の障害物のy座標のlist
obstacles_column = defaultdict(list) #obstacles_column[Y] := 左からY列目の障害物のx座標のlist
for _ in range(N):
    X, Y = map(int, input().split())
    obstacles_row[X].append(Y)
    obstacles_column[Y].append(X)

for X in obstacles_row:
    obstacles_row[X].sort()
for Y in obstacles_column:
    obstacles_column[Y].sort()

ans = {(s_x, s_y): 0}
q = deque([(s_x, s_y)])
while q:
    x, y = q.popleft()

    #上
    u = bisect.bisect_right(obstacles_column[y], x)
    if u > 0 and (obstacles_column[y][u-1] + 1, y) not in ans:
        ans[(obstacles_column[y][u-1] + 1, y)] = ans[(x, y)] + 1
        q.append((obstacles_column[y][u-1] + 1, y))

    #下
    d = bisect.bisect_left(obstacles_column[y], x)
    if d < len(obstacles_column[y]) and (obstacles_column[y][d] - 1, y) not in ans:
        ans[(obstacles_column[y][d] - 1, y)] = ans[(x, y)] + 1
        q.append((obstacles_column[y][d] - 1, y))
    
    #左
    l = bisect.bisect_right(obstacles_row[x], y)
    if l > 0 and (x, obstacles_row[x][l-1] + 1) not in ans:
        ans[(x, obstacles_row[x][l-1] + 1)] = ans[(x, y)] + 1
        q.append((x, obstacles_row[x][l-1] + 1))
    
    #右
    r = bisect.bisect_left(obstacles_row[x], y)
    if r < len(obstacles_row[x]) and (x, obstacles_row[x][r] - 1) not in ans:
        ans[(x, obstacles_row[x][r] - 1)] = ans[(x, y)] + 1
        q.append((x, obstacles_row[x][r] - 1))

print(ans[(g_x, g_y)] if (g_x, g_y) in ans else -1)