import itertools

print(sorted((sum(c) for c in itertools.combinations(map(int, input().split()), 3)), reverse=True)[2])