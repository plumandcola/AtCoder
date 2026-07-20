def is_less_than_180_degree(i: int) -> bool:
    v1 = [x[(i+1) % 4] - x[i], y[(i+1) % 4] - y[i]]
    v2 = [x[(i-1) % 4] - x[i], y[(i-1) % 4] - y[i]]
    return (v1[0] * v2[1] - v1[1] * v2[0]) > 0


x = [0] * 4
y = [0] * 4
for i in range(4):
    x[i], y[i] = map(int, input().split())

print("Yes" if all(is_less_than_180_degree(i) for i in range(4)) else "No")