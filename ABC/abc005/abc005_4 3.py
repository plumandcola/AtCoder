N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

s = [[0] * (N + 1) for _ in range(N + 1)] #二次元累積和
for i in range(N):
    for j in range(N):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + D[i][j]

ans = [0] * (N * N + 1)
"""ans[i] := 面積がi以下の長方形で焼けるたこ焼きの美味しさの合計の最大値"""

for u in range(N): #長方形の上
    for l in range(N): #長方形の左
        for d in range(u, N): #長方形の下
            for r in range(l, N): #長方形の右
                area = (d - u + 1) * (r - l + 1) #長方形の面積
                ans[area] = max(ans[area], s[d+1][r+1] - s[d+1][l] - s[u][r+1] + s[u][l])

for i in range(N * N):
    ans[i+1] = max(ans[i+1], ans[i])

Q = int(input())
for _ in range(Q):
    P = int(input())
    print(ans[P])