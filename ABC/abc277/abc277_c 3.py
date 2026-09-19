from collections import defaultdict

N = int(input())

g = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

visited = {1}
q = [1] #dfs(スタック)
while q:
    v = q.pop()
    for u in g[v]:
        if u not in visited:
            visited.add(u)
            q.append(u)

print(max(visited))