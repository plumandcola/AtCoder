N, Q = map(int, input().split())
a = [0] * N

for _ in range(Q):
    L, R, T = map(int, input().split())
    for i in range(L-1, R):
        a[i] = T

print(*a, sep="\n")