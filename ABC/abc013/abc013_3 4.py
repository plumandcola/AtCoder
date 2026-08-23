#100点解法
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = float("inf")
for i in range(N+1): #普通の食事をとる日数
    for j in range(N-i+1): #質素な食事をとる日数
        ans_ij = A * i + C * j #食費の合計
        s = H + B * i + D * j - E * (N - i - j) #満腹度
        if s > 0:
            ans = min(ans, ans_ij)

print(ans)
