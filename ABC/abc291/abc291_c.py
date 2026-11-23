N = int(input())

x = 0
y = 0
visited = {(0, 0)}
for c in input():
    match c:
        case 'R': x += 1
        case 'L': x -= 1
        case 'U': y += 1
        case 'D': y -= 1

    if (x, y) in visited:
        print("Yes")
        break
    else:
        visited.add((x, y))
else:
    print("No")
