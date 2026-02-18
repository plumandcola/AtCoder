import itertools, math

N, X = map(int, input().split())

L = [0] * N
a = [[] for _ in range(N)]
for i in range(N):
    L[i], *a[i] = map(int, input().split())

print(sum(math.prod(p) == X for p in itertools.product(*a)))