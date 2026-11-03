N = int(input())

ans = [0] * 6
for _ in range(N):
    MT, mT = map(float, input().split())
    if MT >= 35:
        ans[0] += 1
    elif 35 > MT >= 30:
        ans[1] += 1
    elif 30 > MT >= 25:
        ans[2] += 1
    
    if mT >= 25:
        ans[3] += 1
    elif mT < 0 and MT >= 0:
        ans[4] += 1
    elif MT < 0:
        ans[5] += 1

print(*ans)