x, y, W = input().split()
x = int(x) - 1
y = int(y) - 1

c = [input() for _ in range(9)]

if "R" in W:
    dx = 1
elif "L" in W:
    dx = -1
else:
    dx = 0

if "D" in W:
    dy = 1
elif "U" in W:
    dy = -1
else:
    dy = 0


ans = c[y][x]
for _ in range(3):
    if (not 0 <= x + dx < 9) or (not 0 <= y + dy < 9):
        #進んでいた方向が上下左右の場合
        if dx == 0 or dy == 0:
            dx *= -1
            dy *= -1
        
        #進んでいた方向が斜めの場合
        else:
            #角で向きを変更する場合
            if not (0 <= x + dx < 9) and not (0 <= y + dy < 9):
                dx *= -1
                dy *= -1
            
            #左右の端で向きを変更する場合
            elif not (0 <= x + dx < 9):
                dx *= -1
            
            #上下の端で向きを変更する場合
            elif not (0 <= y + dy < 9):
                dy *= -1
    
    x += dx
    y += dy
    ans += c[y][x]

print(ans)