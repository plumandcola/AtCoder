ans = 0

for c in input():
    match c:
        case 'v':
            ans += 1
        case 'w':
            ans += 2

print(ans)