S = [input() for _ in range(2)]

first_black = True
visited = [[False] * 2 for _ in range(2)]
for i in range(2):
    for j in range(2):
        if S[i][j] == '#' and first_black == True:
            first_black = False
            q = [(i, j)]
            visited[i][j] = True
            while q:
                y, x = q.pop()
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= y+dy < 2 and 0 <= x+dx < 2 and S[y+dy][x+dx] == '#' and visited[y+dy][x+dx] == False:
                        visited[y+dy][x+dx] = True
                        q.append((y+dy, x+dx))

ans = True
for i in range(2):
    for j in range(2):
        if S[i][j] == '#' and visited[i][j] == False:
            ans = False

print("Yes" if ans else "No")