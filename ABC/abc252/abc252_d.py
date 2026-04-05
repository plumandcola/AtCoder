from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

ans = N * (N-1) * (N-2) // 6
for a in A:
    ans -= A[a] * (A[a] - 1) // 2 * (N - A[a])
    ans -= A[a] * (A[a] - 1) * (A[a] - 2) // 6

print(ans)