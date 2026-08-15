tx_a, ty_a, tx_b, ty_b, T, V = map(int, input().split())

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if ((x - tx_a) ** 2 + (y - ty_a) ** 2) ** 0.5 + ((x - tx_b) ** 2 + (y - ty_b) ** 2) ** 0.5 <= V * T:
        print("YES")
        break
else:
    print("NO")
