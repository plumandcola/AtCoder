N = int(input())

A = [0] * N
B = [0] * N
floors = {1}
for i in range(N):
    A[i], B[i] = map(int, input().split())
    floors.add(A[i])
    floors.add(B[i])

floors_sorted = sorted(floors)
floors_dict = {f: i for i, f in enumerate(floors_sorted)}

g = [[] for _ in range(len(floors_sorted))]
for i in range(N):
    a = floors_dict[A[i]]
    b = floors_dict[B[i]]
    g[a].append(b)
    g[b].append(a)

visited = [False] * len(floors_sorted)
visited[0] = True
q = [0] #dfs(スタック)
while q:
    v = q.pop()
    for u in g[v]:
        if visited[u] == False:
            visited[u] = True
            q.append(u)

for i in range(len(floors_sorted) - 1, -1, -1):
    if visited[i] == True:
        print(floors_sorted[i])
        break
