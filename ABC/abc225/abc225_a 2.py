import itertools

S = input()

ans = set()
for p in itertools.permutations(S):
    ans.add("".join(p))

print(len(ans))