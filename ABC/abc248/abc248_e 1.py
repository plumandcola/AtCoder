N, K = map(int, input().split())

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

if K == 1:
    print("Infinity")
else:
    ans = 0
    checked = [[False] * N for _ in range(N)] #点iと点jを通る直線を確かめたかどうか
    #全ての2点のペアについて、直線の式を求める
    for i in range(N-1):
        for j in range(i+1, N):
            if checked[i][j] == True: #すでに調べた直線
                continue

            points = {i, j} #点iと点jを通る直線が通る点
            if X[i] == X[j]: #点iと点jを通る直線が、y軸に平行な時
                for k in range(N):
                    if X[k] == X[i]:
                        points.add(k)
            else:
                a = Y[i] - Y[j]
                b = -X[i] + X[j]
                c = -(Y[i] - Y[j]) * X[i] + (X[i] - X[j]) * Y[i]

                for k in range(N):
                    if a * X[k] + b * Y[k] + c == 0:
                        points.add(k)
            
            #この直線が通る点の全てのペアについて、確かめたと記録する
            for k in points:
                for l in points:
                    checked[k][l] = True
                    checked[l][k] = True
            
            if len(points) >= K:
                ans += 1
    print(ans)
