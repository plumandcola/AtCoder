import heapq

def bfs(x: int) -> bool:
    d = [[-1] * W for _ in range(H)]
    q = [(0, si, sj)]
    while q:
        t, i, j = heapq.heappop(q)
        if d[i][j] != -1: continue #すでに探索済み

        d[i][j] = t
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W or d[ni][nj] != -1: continue

            if s[ni][nj] != '#':
                heapq.heappush(q, (t + 1, ni, nj))
            elif s[ni][nj] == '#':
                heapq.heappush(q, (t + x, ni, nj))
    
    return d[gi][gj] <= T


H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j] == 'S':
            si = i
            sj = j
        elif s[i][j] == 'G':
            gi = i
            gj = j

l = 0
r = T
while r - l > 1:
    mid = (l + r) // 2
    if bfs(mid): #T秒以内にゴール地点に到着することが可能
        l = mid
    else:
        r = mid

print(l)