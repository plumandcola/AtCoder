N, X = map(int, input().split())

for i, P in enumerate(map(int, input().split()), 1):
    if P == X:
        print(i)
