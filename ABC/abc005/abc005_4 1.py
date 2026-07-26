#50点解法
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
for _ in range(Q):
    P = int(input())
    ans = 0
    for u in range(N): #長方形の上
        for l in range(N): #長方形の左
            for d in range(u, N): #長方形の下
                for r in range(l, N): #長方形の右
                    if (d - u + 1) * (r - l + 1) <= P: #長方形の面積がP以下なら答えを更新
                        ans = max(ans, sum(sum(D[i][j] for j in range(l, r+1)) for i in range(u, d+1)))
    print(ans)