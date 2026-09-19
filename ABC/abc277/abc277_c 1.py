from collections import defaultdict, deque

N = int(input())

g = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

visited = {1}
q = deque([1]) #bfs
while q:
    v = q.popleft()
    for u in g[v]:
        if u not in visited:
            visited.add(u)
            q.append(u)

print(max(visited))