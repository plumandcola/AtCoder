N, M = map(int, input().split())

danced = [[False] * N for _ in range(N)]
for _ in range(M):
    k, *x = map(int, input().split())
    for i in range(k-1):
        for j in range(i+1, k):
            danced[x[i] - 1][x[j] - 1] = True

ans = "Yes"
for i in range(N-1):
    for j in range(i+1, N):
        if danced[i][j] == False:
            ans = "No"

print(ans)