N = int(input())
S = list(map(int, input().split()))

A = S[:]
for i in range(N):
    for j in range(i):
        A[i] -= A[j]

print(*A)