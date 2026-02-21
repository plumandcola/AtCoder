from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

for i in range(1, N+1):
    if A[i] == 3:
        print(i)