N, D = map(int, input().split())
walls = sorted(tuple(map(int, input().split())) for _ in range(N))

ans = 0
l = float("inf")
for L, R in walls[::-1]:
    if R < l: #前回までのパンチで破壊できる範囲にないなら
        ans += 1
        l = L - D + 1

print(ans)