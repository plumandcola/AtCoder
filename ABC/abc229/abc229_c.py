N, W = map(int, input().split())

AB = sorted([tuple(map(int, input().split())) for _ in range(N)], reverse=True)

ans = 0
for i in range(N):
    A, B = AB[i]
    ans += A * min(B, W)
    W -= min(B, W)

print(ans)