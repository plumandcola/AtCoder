import bisect

N = int(input())
xy = sorted(tuple(map(int, input().split())) for _ in range(N))

ans = 0
for i in range(N):
    x_i, y_i = xy[i]
    for j in range(N):
        x_j, y_j = xy[j]
        if x_i < x_j and y_i < y_j:
            index1 = bisect.bisect_left(xy, (x_i, y_j))
            index2 = bisect.bisect_left(xy, (x_j, y_i))
            if index1 < N and index2 < N and xy[index1] == (x_i, y_j) and xy[index2] == (x_j, y_i):
                ans += 1

print(ans)