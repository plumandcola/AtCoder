from collections import defaultdict
import bisect

N = int(input())
A = list(map(int, input().split()))

indices = defaultdict(list)
for i in range(N):
    indices[A[i]].append(i)

Q = int(input())
for _ in range(Q):
    L, R, X = map(int, input().split())
    print(bisect.bisect_left(indices[X], R) - bisect.bisect_left(indices[X], L-1))