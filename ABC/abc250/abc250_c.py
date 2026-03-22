N, Q = map(int, input().split())

a = list(range(1, N+1))
indices = list(range(N))
for _ in range(Q):
    x = int(input())
    i = indices[x - 1]
    if i != N - 1:
        a[i], a[i + 1] = a[i + 1], a[i]
        indices[x - 1] = i + 1
        indices[a[i] - 1] = i
    else:
        a[i - 1], a[i] = a[i], a[i - 1]
        indices[x - 1] = i - 1
        indices[a[i] - 1] = i

print(*a)