N, M = map(int, input().split())

g = [[0] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A-1][B-1] = 1
    g[B-1][A-1] = 1

for i in range(N): #i番目のユーザについて調べる
    ans = [False] * N
    for j in range(N): #j番目のユーザが「友達の友達」かどうかを調べる
        for k in range(N): #i番目のユーザとk番目のユーザが友達、かつk番目のユーザとj番目のユーザが友達かどうかを調べる
            if g[i][k] == 1 and g[k][j] == 1 and j != i and g[i][j] == 0:
                #自分自身や友達でないことも確認
                ans[j] = True
    print(sum(ans))