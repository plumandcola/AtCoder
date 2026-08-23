#101点解法
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = float("inf")
for i in range(N+1): #普通の食事をとる日数
    diff = E * N - (B+E) * i - H #満腹度が0以下にならないために、さらに必要な満腹度
    if diff < 0:
        ans = min(ans, A * i) #質素な食事をとる必要がない
        continue

    j = diff // (D + E) + 1 #満腹度が0以下にならないために、質素な食事をとる必要のある日数
    if j <= N:
        ans = min(ans, A * i + C * j)

print(ans)