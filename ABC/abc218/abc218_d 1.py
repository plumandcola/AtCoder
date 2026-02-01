N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

xy_set = set(xy)

ans = 0
for i in range(N):
    x_i, y_i = xy[i]
    for j in range(N):
        x_j, y_j = xy[j]
        if x_i < x_j and y_i < y_j and (x_i, y_j) in xy_set and (x_j, y_i) in xy_set:
            ans += 1

print(ans)