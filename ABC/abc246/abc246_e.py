from collections import deque

N = int(input())
A_x, A_y = map(int, input().split())
B_x, B_y = map(int, input().split())
S = [input() for _ in range(N)]

ans = [[-1] * N for _ in range(N)]
ans[A_x - 1][A_y - 1] = 0

visited_1 = [[False] * N for _ in range(N)] #左上から右下の方向に調べたか
visited_1[A_x - 1][A_y - 1] = True
visited_2 = [[False] * N for _ in range(N)] #左下から右上の方向に調べたか
visited_2[A_x - 1][A_y - 1] = True

q = deque([(A_x - 1, A_y - 1)])
while q:
    x, y = q.popleft()

    d = 1
    while 0 <= x+d < N and 0 <= y+d < N and S[x+d][y+d] != '#' and visited_1[x+d][y+d] == False:
        visited_1[x+d][y+d] = True
        if ans[x+d][y+d] == -1:
            ans[x+d][y+d] = ans[x][y] + 1
            q.append((x+d, y+d))
        d += 1

    d = 1
    while 0 <= x+d < N and 0 <= y-d < N and S[x+d][y-d] != '#' and visited_2[x+d][y-d] == False:
        visited_2[x+d][y-d] = True
        if ans[x+d][y-d] == -1:
            ans[x+d][y-d] = ans[x][y] + 1
            q.append((x+d, y-d))
        d += 1

    d = 1
    while 0 <= x-d < N and 0 <= y+d < N and S[x-d][y+d] != '#' and visited_2[x-d][y+d] == False:
        visited_2[x-d][y+d] = True
        if ans[x-d][y+d] == -1:
            ans[x-d][y+d] = ans[x][y] + 1
            q.append((x-d, y+d))
        d += 1

    d = 1
    while 0 <= x-d < N and 0 <= y-d < N and S[x-d][y-d] != '#' and visited_1[x-d][y-d] == False:
        visited_1[x-d][y-d] = True
        if ans[x-d][y-d] == -1:
            ans[x-d][y-d] = ans[x][y] + 1
            q.append((x-d, y-d))
        d += 1

print(ans[B_x - 1][B_y - 1])