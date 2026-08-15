from collections import deque

N, M = map(int, input().split())

root_M = set()
for i in range(N):
    for j in range(N):
        if i * i + j * j == M:
            root_M.add((i, j))
            root_M.add((-i, -j))
            root_M.add((j, -i))
            root_M.add((-j, i))

ans = [[-1] * N for _ in range(N)]
ans[0][0] = 0
q = deque([(0, 0)])
while q:
    i, j = q.popleft()
    for di, dj in root_M:
        if 0 <= i + di < N and 0 <= j + dj < N and ans[i + di][j + dj] == -1:
            ans[i + di][j + dj] = ans[i][j] + 1
            q.append((i + di, j + dj))

for i in range(N):
    print(*ans[i])
