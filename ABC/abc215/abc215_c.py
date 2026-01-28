import itertools

S, K = input().split()

strings = set()
for p in itertools.permutations(S):
    strings.add("".join(p))

print(sorted(strings)[int(K) - 1])