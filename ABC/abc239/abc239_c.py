x_1, y_1, x_2, y_2 = map(int, input().split())

ans1 = set()
for dx, dy in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
    ans1.add((x_1 + dx, y_1 + dy))

ans2 = set()
for dx, dy in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
    ans2.add((x_2 + dx, y_2 + dy))

print("Yes" if ans1 & ans2 else "No")