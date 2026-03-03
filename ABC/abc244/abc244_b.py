N = int(input())
T = input()

x = 0
y = 0
d = ((1, 0), (0, -1), (-1, 0), (0, 1)) #東・南・西・北を向いている時の、x座標・y座標の変化
i = 0 #今の向き
for t in T:
    if t == 'S':
        dx, dy = d[i]
        x += dx
        y += dy
    elif t == 'R':
        i = (i+1) % 4

print(x, y)