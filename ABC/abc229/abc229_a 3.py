def dfs(i, j):
    visited[i][j] = True
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= i+di < 2 and 0 <= j+dj < 2 and S[i+di][j+dj] == '#' and visited[i+di][j+dj] == False:
            dfs(i+di, j+dj)


S = [input() for _ in range(2)]

first_black = True
visited = [[False] * 2 for _ in range(2)]
for i in range(2):
    for j in range(2):
        if S[i][j] == '#' and first_black == True:
            first_black = False
            dfs(i, j)

ans = True
for i in range(2):
    for j in range(2):
        if S[i][j] == '#' and visited[i][j] == False:
            ans = False

print("Yes" if ans else "No")