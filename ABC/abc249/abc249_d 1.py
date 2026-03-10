from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

M = max(A)

ans = 0
for q in range(1, M+1):
    for r in range(1, M // q + 1):
        ans += A[q * r] * A[q] * A[r]

print(ans)