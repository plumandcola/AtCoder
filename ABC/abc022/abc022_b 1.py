N = int(input())

ans = 0
visited = [False] * 100000
for _ in range(N):
    A = int(input())
    if visited[A-1] == False:
        visited[A-1] = True
    else:
        ans += 1

print(ans)