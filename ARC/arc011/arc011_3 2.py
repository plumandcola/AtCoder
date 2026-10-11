from collections import deque

first, last = input().split()
N = int(input())
s = [input() for _ in range(N)] + [first] + [last]

l = len(first)

g = [[] for _ in range(N+2)]
for i in range(N+1):
    for j in range(i+1, N+2):
        if sum(s[i][k] == s[j][k] for k in range(l)) >= l - 1:
            g[i].append(j)
            g[j].append(i)

q = deque([N+1])
d = [-1] * (N+2)
d[N+1] = 0
while q:
    v = q.popleft()
    for u in g[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            q.append(u)

if d[N] != -1:
    print(d[N] - 1)
    v = N
    while True:
        print(s[v])
        for u in g[v]:
            if d[u] == d[v] - 1:
                v = u
                break
        else:
            break
else:
    print(-1)
