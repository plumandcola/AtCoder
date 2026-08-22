from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

for v, f in sorted(A.items(), reverse=True):
    print(f)

for _ in range(N - len(A)):
    print(0)
