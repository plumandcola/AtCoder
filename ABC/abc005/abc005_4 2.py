N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

s = [[0] * (N + 1) for _ in range(N + 1)] #二次元累積和
for i in range(N):
    for j in range(N):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + D[i][j]

Q = int(input())
for _ in range(Q):
    P = int(input())
    ans = 0
    for H in range(1, min(N, P)+1): #長方形の縦の長さ
        W = min(N, P // H) #長方形の横の長さ(できるだけ長い方がいい)
        for i in range(N-H+1): #長方形の上
            for j in range(N-W+1): #長方形の左
                ans = max(ans, s[i+H][j+W] - s[i+H][j] - s[i][j+W] + s[i][j])
    print(ans)