#10点解法
N = int(input())
f_x = [0] * N
f_y = [0] * N

for i in range(N):
    f_x[i], f_y[i] = map(int, input().split())

M = int(input())
s_x = [0] * M
s_y = [0] * M

for i in range(M):
    s_x[i], s_y[i] = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(N):
    m = float("inf")
    for j in range(M):
        m = min(m, (f_x[i] - s_x[j]) ** 2 + (f_y[i] - s_y[j]) ** 2)
    
    for j in range(N):
        if (f_x[i] - f_x[j]) ** 2 + (f_y[i] - f_y[j]) ** 2 < m:
            g[i].append(j)

ans = N
for b in range(1 << N):
    visited = [False] * N
    count = 0 #機密情報を直接伝えた仲間の人数
    for i in range(N):
        if (b >> i) & 1 == 1:
            count += 1
            q = [i]
            while q:
                v = q.pop()
                if visited[v] == True: continue

                visited[v] = True
                for u in g[v]:
                    if visited[u] == False:
                        q.append(u)
    
    if sum(visited) == N:
        ans = min(ans, count)

print(ans)