#50点解法
N, M = map(int, input().split())

ans_min = 1
ans_max = 1
a = [1] * N
b = [0] * N
for _ in range(M):
    query = input().split()
    p = int(query[0]) - 1
    a[p] = float(query[1])
    b[p] = float(query[2])

    r = 1
    for i in range(N):
        r = a[i] * r + b[i]

    ans_min = min(ans_min, r)
    ans_max = max(ans_max, r)

print(ans_min)
print(ans_max)