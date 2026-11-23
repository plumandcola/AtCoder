N, M = map(int, input().split())
A = list(map(int, input().split()))

print(sum(A[B-1] for B in map(int, input().split())))