N = int(input())
A = [int(input()) for _ in range(N)]

A_set = set(A)

A_sorted = list(A_set)
A_sorted.sort(reverse=True)

print(A_sorted[1])