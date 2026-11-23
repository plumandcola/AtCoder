import itertools

N = int(input())

xy = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i, j, k in itertools.combinations(range(N), 3):
    s = (xy[j][0] - xy[i][0]) * (xy[k][1] - xy[i][1]) - (xy[k][0] - xy[i][0]) * (xy[j][1] - xy[i][1])
    if s % 2 == 0 and s != 0:
        ans += 1

print(ans)