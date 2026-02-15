N, D = map(int, input().split())
walls = sorted((tuple(map(int, input().split())) for _ in range(N)), key = lambda x: x[1])

ans = 0
r = -float("inf")
for L, R in walls:
    if L > r: #前回までのパンチで破壊できる範囲にないなら
        ans += 1
        r = R + D - 1

print(ans)