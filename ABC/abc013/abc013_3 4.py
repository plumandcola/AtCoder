#100点解法
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = float("inf")
for i in range(N+1): #普通の食事をとる日数
    for j in range(N-i+1): #質素な食事をとる日数
        if H + B * i + D * j - E * (N - i - j) > 0: #満腹度が0以下にならないようにできる
            ans = min(ans, A * i + C * j)

print(ans)
