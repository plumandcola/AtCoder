from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)

ans = [0] * N
for i, a in enumerate(sorted(set(A), reverse=True)):
    ans[i] = count[a]

print(*ans, sep="\n")