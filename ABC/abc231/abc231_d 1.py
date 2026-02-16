from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

ans = True
visited = [False] * N
for i in range(N):
    if len(g[i]) > 2: #隣り合わないといけない人が2人を超えるなら不可能
        ans = False
        break
    
    if visited[i] == True:
        continue
    
    q = deque([(i, -1)]) #閉路がないか確認
    while q:
        v, parent = q.popleft()
        for u in g[v]:
            if u != parent:
                if visited[u] == True: #閉路あり
                    ans = False
                else:
                    visited[u] = True
                    q.append((u, v))

print("Yes" if ans else "No")