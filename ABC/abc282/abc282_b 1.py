N, M = map(int, input().split())

S = [input() for _ in range(N)]

ans = 0
for x in range(N-1):
    for y in range(x+1, N):
        for j in range(M):
            if S[x][j] == 'x' and S[y][j] == 'x':
                break
        else:
            ans += 1

print(ans)