import itertools

N, M = map(int, input().split())

for c in itertools.combinations(range(1, M+1), N):
    print(*c)
