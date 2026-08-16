N = int(input())
NG = {int(input()) for _ in range(3)}

M = 3 #選べる数字の上限
steps = [float("inf")] * (N+1)
steps[N] = 0
for i in range(N, 0, -1):
    if steps[i] == float("inf") or i in NG:
        continue

    for j in range(i-1, max(0, i-M) - 1, -1):
        steps[j] = min(steps[j], steps[i] + 1)

print("YES" if 0 <= steps[0] <= 100 else "NO")