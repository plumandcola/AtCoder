import math

N, K = map(int, input().split())

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

if K == 1:
    print("Infinity")
else:
    ans = set() #条件を満たす直線
    #全ての2点のペアについて、直線の式を求める
    for i in range(N-1):
        for j in range(i+1, N):
            if X[i] == X[j]: #点iと点jを通る直線が、y軸に平行な時
                count = sum(X[k] == X[i] for k in range(N))
                if count >= K:
                    ans.add(X[i])
            else:
                a = Y[i] - Y[j]
                b = -X[i] + X[j]
                c = -(Y[i] - Y[j]) * X[i] + (X[i] - X[j]) * Y[i]

                #同じ直線を重複して数えないように、gcdで割る
                g = math.gcd(a, b, c)
                a //= g
                b //= g
                c //= g

                count = sum(a * X[k] + b * Y[k] + c == 0 for k in range(N))
                if count >= K and (-a, -b, -c) not in ans: #符号違いで区別されないように
                    ans.add((a, b, c))
    print(len(ans))